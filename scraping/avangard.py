from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://avangardstyle.kg/builds/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(response)

buildingListings = soup.find_all('div', class_ = 'wpb_wrapper')

buildingList = list()

for i in buildingListings:
    for j in i.find_all('div', class_ = 'building-objects'):
        for k in j.find_all('div', class_ = 'object-card'):
            for z in k.find_all('div', class_ = 'object-card_content'):
                for p in z.find_all('div', class_ = 'object-card_desc'):
                    # print(p.text)
                    buildingList.append(p.text)

print(buildingList)

for i in buildingList:
    print(i.lstrip(), end='\n' )
