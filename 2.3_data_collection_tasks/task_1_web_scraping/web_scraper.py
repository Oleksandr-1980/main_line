import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    try:
        # Виконати HTTP-запит до вебсайту
        response = requests.get(url)
        response.raise_for_status()  # Перевірка на помилки HTTP

        # Аналіз HTML-коду сторінки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Знайти заголовки новин (адаптуйте тег і клас залежно від структури сайту)
        headlines = soup.find_all('h2', class_='news-title')  # Приклад класу
        
        # Зібрати текст заголовків
        news_headlines = [headline.get_text(strip=True) for headline in headlines]
        return news_headlines

    except requests.exceptions.RequestException as e:
        print(f"Помилка при підключенні до вебсайту: {e}")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

if __name__ == '__main__':
    # URL сторінки новин на сайті ЗСУ
    url = 'https://www.zsu.gov.ua/category/news/page/2/'  # Замініть на реальний URL
    headlines = get_news_headlines(url)

    if headlines:
        print("Заголовки новин:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")
    else:
        print("Не вдалося знайти заголовки новин.")
