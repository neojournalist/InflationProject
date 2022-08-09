from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())
quotes = soup.findAll('span', class_ = 'text')
author = soup.find_all('small', class_ = 'author')
tags = soup.find_all('div', class_ = 'tags')
#print(quotes)

# ListQuotation = list()
# for quote in quotes:
#     print(quote.text)

ListQuotation = list()

# for quote in quotes:
#     ListQuotation.append(quote.text)
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('(stated by)' + author[i].text)
    tagsQuotes = tags[i].find_all('a', class_ = 'tag')

    for i in tagsQuotes:
        print(i.text)
    print('\n')


# for q in ListQuotation:
#     print(q, end='\n')

# print(ListQuotation[1])
