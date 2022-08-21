from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/country/kyrgyzstan/'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'lxml')

#print(soup.text)

cases = soup.find_all('div', class_ = 'maincounter-number')
print(cases)
data = []

for case in cases:
    span = case.find('span')
    data.append(span.string)

print(data)
df = pd.DataFrame({"CovidData for Kyrgyzstan": data})
df.index = ['Total cases', 'Deaths', 'Recovered']
df.to_csv('covidCases_Kyrgyzstan.csv')