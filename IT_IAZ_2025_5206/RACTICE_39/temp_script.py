import cv2
import numpy as np
import matplotlib.pyplot as plt

# Завантаження зображення з файлу
image_path = 'photo-car.jpg'
image = cv2.imread(image_path)

# Перевірка, чи зображення завантажено успішно
if image is None:
    print("Помилка: Не вдалося завантажити зображення. Перевірте шлях до файлу.")
    exit(1)

# Відображення за допомогою matplotlib (конвертуємо з BGR в RGB)
plt.figure(figsize=(8, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Завантажене зображення")
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
plt.title('Зображення у відтінках сірого')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(resized, cmap='gray')
plt.title('Зображення зі зміненим розміром')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(blurred, cmap='gray')
plt.title('Розмите зображення')
plt.axis('off')

plt.tight_layout()
plt.show()

# Виявлення країв за допомогою Canny
edges = cv2.Canny(gray, 50, 150)

# Відображення результату за допомогою matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(edges, cmap='gray')
plt.title("Виявлені краї")
plt.axis('off')
plt.show()

# Пропускаємо виявлення автомобілів через проблеми з каскадним класифікатором
# Замість цього просто відображаємо оригінальне зображення
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Оригінальне зображення автомобіля")
plt.axis('off')
plt.show()