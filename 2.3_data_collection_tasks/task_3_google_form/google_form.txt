function createGoogleForm() {
  // Назва форми
  const formTitle = "Форма для збору даних";

  // Створення нової форми
  const form = FormApp.create(formTitle);

  // Додавання текстового поля для введення імені
  form.addTextItem()
      .setTitle("Ім'я")
      .setRequired(true);

  // Додавання поля для вибору дати
  form.addDateItem()
      .setTitle("Дата")
      .setRequired(true);

  // Додавання поля для вибору відділу
  form.addMultipleChoiceItem()
      .setTitle("Відділ")
      .setChoiceValues([
        "Маркетинг",
        "Продажі",
        "Розробка",
        "Інший"
      ])
      .setRequired(true);

  // Отримання посилання на форму
  const formUrl = form.getPublishedUrl();
  Logger.log("Форма створена: " + formUrl);

  // Вивід посилання на форму у консоль
  console.log("Посилання на форму: " + formUrl);
}