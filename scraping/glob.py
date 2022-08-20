from bs4 import BeautifulSoup
import lxml
import requests
import pandas

import datetime
import os
from pydrive import drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def file_upload():
    gauth = GoogleAuth
    drive = GoogleDrive(gauth)


    url_drink = 'https://globus-online.kg/catalog/napitki/kola_limonady/'
    response_drink = requests.get(url)
    soup_drink = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())
    prod_name = soup.find_all('div', class_='list-showcase__name')
    prod_list_name = [pn.text for pn in prod_name]
    prod_price = soup.find('span', class_='c-prices__value-currency')
    prod_list_price = [int(pp.text[:3]) for pp in prod_price]
    print(int(prod_price.text))

    prod_info = pd.DataFrame(
        {
            'Product name': prod_list_name,
            'Price(soms)': prod_list_price
        }
    )

    prod_info.to_excel('prodInfo.xlsx', index=False)

    folder = ''
    filePath = ''
    file_origin = os.path.join(filePath, 'prodInfo.xlsx')

    now = datetime.datetime.now()
    date_time_string = now.strftime("%d/%m/%Y-%H:%M")

    excel_document = drive.CreateFile({'parents':[{'id':folder}], 'title': 'Product_Info'})
    excel_document.SetContentFile(file_origin)
    excel_document.Upload()
    print('Success!')

if __name__ == '__main__':
    #upload_drive()
    schedule.every(5).seconds.do(upload_drive)

    while True:
        schedule.run_pending()
        time.sleep(1)


