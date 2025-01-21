from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = '111'  # Для повідомлень Flash

# Конфігурація бази даних
DB_CONFIG = {
    'dbname': 'PersonnelManagementDB',
    'user': 'postgres',
    'password': 'admin1',
    'host': 'localhost',
    'port': 5432
}

# Функція для підключення до бази даних
def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

# Головна сторінка (Read)
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT PersonnelID, rank, fullname, position, unit, deploymentstatus FROM Personnel order by PersonnelID")
    records = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', records=records)

# Сторінка для створення запису (Create)
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

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Personnel (rank, fullname, position, unit, deploymentstatus) VALUES (%s, %s, %s, %s, %s)",
            (rank, fullname, position, unit, deploymentstatus)
        )
        conn.commit()
        cur.close()
        conn.close()
        flash('Record created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('create.html')

# Сторінка для редагування запису (Update)
@app.route('/edit/<int:PersonnelID>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        rank = request.form['rank']
        fullname = request.form['fullname']
        position = request.form['position']
        unit = request.form['unit']
        deploymentstatus = request.form['deploymentstatus']

        if not all([rank, fullname, position, unit, deploymentstatus]):
            flash('All fields are required!', 'error')
            return redirect(url_for('edit', id=PersonnelID))

        cur.execute(     
            "UPDATE Personnel SET rank = %s, fullname = %s, position = %s, unit = %s, deploymentstatus = %s  WHERE PersonnelID = %s",
            (rank, fullname, position, unit, deploymentstatus, PersonnelID)
        )
        conn.commit()
        cur.close()
        conn.close()
        flash('Record updated successfully!', 'success')
        return redirect(url_for('index'))

    cur.execute("SELECT PersonnelID, rank, fullname, position, unit, deploymentstatus FROM Personnel WHERE PersonnelID = %s", (id,))
    record = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('edit.html', record=record)

# Видалення запису (Delete)
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Personnel WHERE PersonnelID = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    flash('Record deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
