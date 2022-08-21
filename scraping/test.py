import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import datetime
import os
import schedule
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


url_beef = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/govyadina_baranina_farshi/myaso_govyadina_steyk/'
response_beef = requests.get(url_beef)
soup_beef = bs(response_beef.text, 'html.parser')

data = []

beef = soup_beef.find('span', class_='pagetitle__inner').text
date_collected = datetime.datetime.now()
date_string = date_collected.strftime("%d-%m-%Y")
price_beef = int(soup_beef.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])
link = url_beef

data.append([beef, date_string, price_beef, link])
print(data)

header = ['product', 'date', 'price', 'link']
df = pd.DataFrame(data, columns=header)
df.to_csv('glo_info.csv')



#print(int(prod_price_beef.text[:3]))
#prod_list_price_beef = [pp.text for pp in prod_price_beef]
#
# # prod_link =
# #
# # prod_quantity =
#
#
# prod_glo = pd.DataFrame(
#         {
#             'product': prod_beef,
#             'price': prod_price_beef
#         }
# )
# print(prod_glo)
#prod_glo.to_excel('prodGlo.xlsx')
