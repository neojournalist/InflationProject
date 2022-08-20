import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.kinopoisk.ru/lists/movies/top250/'
r = requests.get(url)
r.text

soup = BeautifulSoup(r.text, 'lxml')

links = soup.find_all('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta_link')
print(links.get('href'))