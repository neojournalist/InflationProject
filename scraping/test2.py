import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('glo-data-360115-0b35385f655d.json', scope)
client = gspread.authorize(credentials)


#sheet = client.create("globus-products")
#sheet.share('mambetova.altynai@gmail.com', perm_type='user', role='writer')

products = []
price = []
links = []


url_beef = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/govyadina_baranina_farshi/myaso_govyadina_steyk/'
response_beef = requests.get(url_beef)
soup_beef = bs(response_beef.text, 'html.parser')

url_lamb = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/govyadina_baranina_farshi/myaso_baranina_lopatochnaya_chast_ves/'
response_lamb = requests.get(url_lamb)
soup_lamb = bs(response_lamb.text, 'html.parser')

url_chicken = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/ptitsa/grudka_kurinaya_eco_meat_okhlozhdennaya_ves/'
response_chicken = requests.get(url_chicken)
soup_chicken = bs(response_chicken.text, 'html.parser')

url_trout = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/ryba_i_moreprodukty/ryba_forel_nepotroshennaya_okhlazhdennaya_ves/'
response_trout = requests.get(url_trout)
soup_trout = bs(response_trout.text, 'html.parser')

url_milk = 'https://globus-online.kg/catalog/molochnye_produkty_yaytsa/moloko_slivki/moloko_umut_i_k_3_2_1l_t_p/'
response_milk = requests.get(url_milk)
soup_milk = bs(response_milk.text, 'html.parser')

url_kefir = 'https://globus-online.kg/catalog/molochnye_produkty_yaytsa/kislomolochnye_produkty/kefir_umut_i_k_2_5_1l_t_p/'
response_kefir = requests.get(url_kefir)
soup_kefir = bs(response_kefir.text, 'html.parser')

url_tvorog = 'https://globus-online.kg/catalog/molochnye_produkty_yaytsa/kislomolochnye_produkty/tvorog/tvorog_veselyy_molochnik_0_2_280g/'
response_tvorog = requests.get(url_tvorog)
soup_tvorog = bs(response_tvorog.text, 'html.parser')

url_butter = 'https://globus-online.kg/catalog/molochnye_produkty_yaytsa/maslo_slivochnoe/maslo_slivochnoe_ak_sut_krestyanskoe_200g/'
response_butter = requests.get(url_butter)
soup_butter = bs(response_butter.text, 'html.parser')

url_eggs = 'https://globus-online.kg/catalog/molochnye_produkty_yaytsa/yaytsa/yaytso_ak_kuu_s_1_10sht/'
response_eggs = requests.get(url_eggs)
soup_eggs = bs(response_eggs.text, 'html.parser')

url_bread = 'https://globus-online.kg/catalog/khleb_khlebobulochnye_izdeliya/khleba_batony_bagety/khleb_soldatskiy_320g/'
response_bread = requests.get(url_bread)
soup_bread = bs(response_bread.text, 'html.parser')

url_lepeshka = 'https://globus-online.kg/catalog/khleb_khlebobulochnye_izdeliya/lepeshki/lepeshka_tandyr_s_belym_kunzhutom_240g_sp/'
response_lepeshka = requests.get(url_lepeshka)
soup_lepeshka = bs(response_lepeshka.text, 'html.parser')

url_rice = 'https://globus-online.kg/catalog/bakaleya/krupy_khlopya/ris_kazakhstanskiy_lider_vesovoy/'
response_rice = requests.get(url_rice)
soup_rice = bs(response_rice.text, 'html.parser')

url_buckwheat = 'https://globus-online.kg/catalog/bakaleya/krupy_khlopya/krupy_vesovye/grechka_vesovaya/'
response_buckwheat = requests.get(url_buckwheat)
soup_buckwheat = bs(response_buckwheat.text, 'html.parser')

url_cucumber = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/ovoshchi/ogurtsy/'
response_cucumber = requests.get(url_cucumber)
soup_cucumber = bs(response_cucumber.text, 'html.parser')

url_tomato = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/ovoshchi/pomidory/'
response_tomato = requests.get(url_tomato)
soup_tomato = bs(response_tomato.text, 'html.parser')

url_onion = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/ovoshchi/luk_repchatyy/'
response_onion = requests.get(url_onion)
soup_onion = bs(response_onion.text, 'html.parser')

url_potato = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/ovoshchi/kartofel_fasovannyy/'
response_potato = requests.get(url_potato)
soup_potato = bs(response_potato.text, 'html.parser')

url_carrot = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/ovoshchi/morkov_mytaya/'
response_carrot = requests.get(url_carrot)
soup_carrot = bs(response_carrot.text, 'html.parser')

url_garlic = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/ovoshchi/chesnok/'
response_garlic = requests.get(url_garlic)
soup_garlic = bs(response_garlic.text, 'html.parser')

url_cabbage = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/ovoshchi/kapusta/'
response_cabbage = requests.get(url_cabbage)
soup_cabbage = bs(response_cabbage.text, 'html.parser')

url_banana = 'https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/frukty_yagody/banany_vysshiy_sort/'
response_banana = requests.get(url_banana)
soup_banana = bs(response_banana.text, 'html.parser')

url_tea = 'https://globus-online.kg/catalog/chay_kofe_kakao_kisel/chay_chernyy/chay_beta_champion_pekoe_listovoy_100g/'
response_tea = requests.get(url_tea)
soup_tea = bs(response_tea.text, 'html.parser')

url_salt = 'https://globus-online.kg/catalog/bakaleya/sousy_pripravy_marinady/sol_bereke_yodirovannaya_750g/'
response_salt = requests.get(url_salt)
soup_salt = bs(response_salt.text, 'html.parser')

url_sugar = 'https://globus-online.kg/catalog/bakaleya/desertnye_produkty/sakhar_navat/sakhar_pesok_vesovoy/'
response_sugar = requests.get(url_sugar)
soup_sugar = bs(response_sugar.text, 'html.parser')

url_oil = 'https://globus-online.kg/catalog/bakaleya/rastitelnye_masla/podsolnechnye_masla/maslo_podsolnechnoe_russkoe_maslo_1l/'
response_oil = requests.get(url_oil)
soup_oil = bs(response_oil.text, 'html.parser')

beef = soup_beef.find('span', class_='pagetitle__inner').text
price_beef = int(soup_beef.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

lamb = soup_lamb.find('span', class_='pagetitle__inner').text
price_lamb = int(soup_lamb.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

chicken = soup_chicken.find('span', class_='pagetitle__inner').text
price_chicken = int(soup_chicken.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

trout = soup_trout.find('span', class_='pagetitle__inner').text
price_trout = int(soup_trout.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

milk = soup_milk.find('span', class_='pagetitle__inner').text
price_milk = int(soup_milk.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

kefir = soup_kefir.find('span', class_='pagetitle__inner').text
price_kefir = int(soup_kefir.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

tvorog = soup_tvorog.find('span', class_='pagetitle__inner').text
price_tvorog = int(soup_tvorog.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

butter = soup_butter.find('span', class_='pagetitle__inner').text
price_butter = int(soup_butter.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

eggs = soup_eggs.find('span', class_='pagetitle__inner').text
price_eggs = int(soup_eggs.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

bread = soup_bread.find('span', class_='pagetitle__inner').text
price_bread = int(soup_bread.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

lepeshka = soup_lepeshka.find('span', class_='pagetitle__inner').text
price_lepeshka = int(soup_lepeshka.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

rice = soup_rice.find('span', class_='pagetitle__inner').text
price_rice = int(soup_rice.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

buckwheat = soup_buckwheat.find('span', class_='pagetitle__inner').text
price_buckwheat = int(soup_buckwheat.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

cucumber = soup_cucumber.find('span', class_='pagetitle__inner').text
price_cucumber = int(soup_cucumber.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

tomato = soup_tomato.find('span', class_='pagetitle__inner').text
price_tomato = int(soup_tomato.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

onion = soup_onion.find('span', class_='pagetitle__inner').text
price_onion = int(soup_onion.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

potato = soup_beef.find('span', class_='pagetitle__inner').text
price_potato = int(soup_beef.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

carrot = soup_carrot.find('span', class_='pagetitle__inner').text
price_carrot = int(soup_carrot.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

garlic = soup_garlic.find('span', class_='pagetitle__inner').text
price_garlic = int(soup_garlic.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

cabbage = soup_cabbage.find('span', class_='pagetitle__inner').text
price_cabbage = int(soup_cabbage.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

banana = soup_banana.find('span', class_='pagetitle__inner').text
price_banana = int(soup_banana.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

tea = soup_tea.find('span', class_='pagetitle__inner').text
price_tea = int(soup_tea.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

salt = soup_salt.find('span', class_='pagetitle__inner').text
price_salt = int(soup_salt.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:2])

sugar = soup_sugar.find('span', class_='pagetitle__inner').text
price_sugar = int(soup_sugar.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

oil = soup_oil.find('span', class_='pagetitle__inner').text
price_oil = int(soup_oil.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text[:3])

products.append([beef, lamb, chicken, trout, milk, kefir, tvorog, butter, eggs, bread, lepeshka, rice, buckwheat,
                 cucumber, tomato, onion, potato, carrot, garlic, cabbage, banana, tea, salt, sugar, oil])

price.append([price_beef, price_lamb, price_chicken, price_trout, price_milk, price_kefir, price_tvorog, price_butter,
              price_eggs, price_bread, price_lepeshka, price_rice, price_buckwheat, price_cucumber, price_tomato,
              price_onion, price_potato, price_carrot, price_garlic, price_cabbage, price_banana, price_tea, price_salt,
              price_sugar, price_oil])

links.append([url_beef, url_lamb, url_chicken, url_trout, url_milk, url_kefir, url_tvorog, url_butter, url_eggs,
              url_bread, url_lepeshka, url_rice, url_buckwheat, url_cucumber, url_tomato, url_onion, url_potato,
              url_carrot, url_garlic, url_cabbage, url_banana, url_tea, url_salt, url_sugar, url_oil])

date_collected = datetime.datetime.now()
date_string = date_collected.strftime("%d-%m-%Y")

products.extend(price)
products.extend(links)

#print(products)

products_df = pd.DataFrame({
    'product':products,
    'price':price,
    'link':links,
    'date':date_string
})

products_df.to_csv('globus_info.csv')

#

# sheet = client.open("globus-products").sheet1

# df = pd.read_csv('globus_info.csv')
# sheet.update([df.columns.values.tolist()] + df.values.tolist())

# print(links)
# print(date)
# extend two lists