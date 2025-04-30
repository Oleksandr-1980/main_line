import cv2
import numpy as np
import matplotlib.pyplot as plt

# Завантаження зображення з файлу
image_path = 'photo-car.jpg'
image = cv2.imread(image_path)

# Відображення за допомогою matplotlib (конвертуємо з BGR в RGB)
plt.figure(figsize=(8, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Loaded Image")
plt.axis('off')
plt.show()

# Перетворення у відтінки сірого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Зміна розміру
resized = cv2.resize(gray, (128, 128))

# Застосування розмиття (Gaussian Blur)
blurred = cv2.GaussianBlur(resized, (5, 5), 0)

# Відображення результатів за допомогою matplotlib
plt.figure(figsize=(15, 5))

# Створюємо підграфіки для трьох зображень
plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title('Gray Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(resized, cmap='gray')
plt.title('Resized Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(blurred, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')

plt.tight_layout()
plt.show()

# Виявлення країв за допомогою Canny
edges = cv2.Canny(gray, 50, 150)

# Відображення результату за допомогою matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(edges, cmap='gray')
plt.title("Edges")
plt.axis('off')
plt.show()

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