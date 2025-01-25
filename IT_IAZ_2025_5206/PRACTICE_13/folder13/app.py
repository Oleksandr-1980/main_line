from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2


app = Flask(__name__)
app.secret_key = '111'  # Для повідомлень Flash

DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin1',
    'host': 'localhost',
    'port': 5432
}

# Функція для підключення до бази даних
def get_db_connection():
    print('connecting...')
    return psycopg2.connect(**DB_CONFIG)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Personnel ORDER BY PersonnelID")
        records = cur.fetchall()
    except Exception as e:
        print(f"Error: {e}", 'error')
        records = []
    finally:
        cur.close()
        conn.close()
    return render_template('index.html', records=records)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        rank = request.form['rank']
        fullname = request.form['fullname']
        position = request.form['position']
        unit = request.form['unit']
        deploymentstatus = request.form['deploymentstatus']

        if not all([rank, fullname, position, unit, deploymentstatus]):
            flash('All fields are required!', 'error')
            return redirect(url_for('create'))

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Personnel (rank, fullname, position, unit, deploymentstatus) VALUES (%s, %s, %s, %s, %s)",
                (rank, fullname, position, unit, deploymentstatus)
            )
            conn.commit()
            flash('Record created successfully!', 'success')
        except Exception as e:
            flash(f"Error while creating record: {e}", 'error')
        finally:
            cur.close()
            conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')