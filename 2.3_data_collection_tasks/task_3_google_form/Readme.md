# Google Apps Script для автоматичного створення Google Форми

Цей скрипт автоматично створює Google Форму для збору даних (ім'я, дата, відділ).

## Налаштування та запуск

### Крок 1: Створення проекту
1. Увійдіть у свій обліковий запис Google.
2. Перейдіть до [Google Apps Script](https://script.google.com).
3. Створіть новий проект, натиснувши **"New Project"**.
4. Скопіюйте та вставте код зі скрипта `google_form.gs` у редактор.

### Крок 2: Збереження та запуск скрипта
1. Натисніть **"File > Save"**, щоб зберегти проект.
2. У меню виберіть функцію `createGoogleForm`.
3. Натисніть **▶ Run** (запустити).

### Крок 3: Надання доступу
Під час першого запуску скрипта:
1. Відкриється вікно авторизації.
2. Виберіть свій обліковий запис Google.
3. Натисніть **"Advanced"** (Додатково) і **"Go to project (unsafe)"**.
4. Надішліть дозвіл на створення та керування Google Формами.

### Крок 4: Отримання URL форми
1. Після успішного виконання скрипта перейдіть до меню **"View > Logs"**.
2. У вікні логів ви побачите посилання на створену форму, наприклад:
   ```
   Форма створена: https://forms.google.com/... 
   ```
3. Скопіюйте посилання та відкрийте його у браузері для перегляду або використання форми.

## Зміна вмісту форми

Щоб налаштувати поля форми:
- Відредагуйте заголовок форми у рядку:
  ```javascript
  const formTitle = "Форма для збору даних";
  ```
- Додайте або змініть поля у функції `createGoogleForm` відповідно до ваших вимог.

## Примітки
- Переконайтеся, що ваш обліковий запис Google має доступ до створення форм.
- У разі помилок перевірте консоль логів у Apps Script.

Якщо виникнуть питання або проблеми, звертайтеся до підтримки або перегляньте [документацію Google Apps Script](https://developers.google.com/apps-script/).