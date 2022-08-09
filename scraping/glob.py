from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://globus-online.kg/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(response.text)