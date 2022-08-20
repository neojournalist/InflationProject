import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import datetime
import os
import schedule
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_drive():
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

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

    prod_beef = soup_beef.find('span', class_='pagetitle__inner')
    prod_beef_list = [pb.text for pb in prod_beef]

    prod_price_beef = soup_beef.find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная')
    prod_list_price_beef = [int(pp.text) for pp in prod_price_beef]

    prod_name = soup_drink.find_all('div', class_='list-showcase__name')
    prod_list_name = [pn.text for pn in prod_name]

    prod_price = soup_drink.find_all('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная')
    prod_list_price = [int(pp.text[:3]) for pp in prod_price]

    prod_list_name.extend(prod_meat_list)
    prod_list_price.extend(prod_list_price_meat)

    prod_info = pd.DataFrame(
        {
            'Имя продукта': prod_list_name,
            'Цена(сом)':prod_list_price
        })

    prod_info.to_excel('prodInfo.xlsx', index=False)

    folder = '1reyeVBqWJTuVcwSAnEMw1t57eZoNhRqi'
    filePath = '/Users/koalas/PycharmProjects/ParsingLesson/Lesson4'
    file_origin = os.path.join(filePath,'prodInfo.xlsx')

    now = datetime.datetime.now()
    date_time_string = now.strftime("%d/%m/%Y-%H:%M:%S")

    excel_document = drive.CreateFile({'parents':[{'id':folder}],
                                       'title':f'Product_Info_{date_time_string}.xlsx'})
    excel_document.SetContentFile(file_origin)
    excel_document.Upload()
    print('Файл загружен!')

if __name__ == '__main__':
    schedule.every(5).seconds.do(upload_drive)

    while True:
        schedule.run_pending()