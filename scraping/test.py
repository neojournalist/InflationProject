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

prod_beef = soup_beef.find('span', class_='pagetitle__inner')
prod_beef_list = [pb.text for pb in prod_beef]

# prod_brand =
#
# prod_store =
#
# prod_date =

prod_price_beef = soup_beef.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная')
prod_list_price_beef = [pp.text for pp in prod_price_beef]

# prod_link =
#
# prod_quantity =



prod_glob = pd.DataFrame(
        {
            'product': prod_beef,
            'price':prod_price_beef
        })

prod_glob.to_excel('prodInfo.xlsx', index=False)
