# Цей файл містить виправлений четвертий блок коду для вашого Jupyter Notebook

# Завантаження попередньо натренованого каскаду для виявлення автомобілів
car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_cars.xml")

# Виявлення автомобілів
cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(80, 80))

# Нанесення рамок на зображення
image_with_cars = image.copy()  # Створюємо копію, щоб не змінювати оригінал
for (x, y, w, h) in cars:
    cv2.rectangle(image_with_cars, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Червоний колір для автомобілів

# Відображення результату за допомогою matplotlib
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(image_with_cars, cv2.COLOR_BGR2RGB))  # Конвертуємо з BGR в RGB
plt.title("Виявлені автомобілі")
plt.axis('off')
plt.show()