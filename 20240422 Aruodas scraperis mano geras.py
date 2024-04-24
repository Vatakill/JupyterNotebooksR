
# geras pavyzdys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
# import undetected_chromedriver as uc
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

opcijos = Options()
opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless')

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Firefox(options=opcijos)

#surinkite iš puslapių nuo 2 iki 11-to butų skelbimus ir tokią informaciją - kaina, kaina už 1 kv metrą, adresas, plotas, 
# kambarių kiekis. 
# šiuos duomenis eksportuokite į csv failą, skirtukas turi būti ;.
#suraskite, kiek iš atrinktų butų buvo pagal kainą pigūs, brangūs, neįperkami. Kriterijus - 1 kv metro kaina iki 1 VDu - pigūs, iki 3 VDU - brangūs, daugiau nei 3 VDU - neįperkami.
#pavaizduokite su boxplotais kainų už 1 kv pasiskirstymą nuo kambarių skaičiaus.
#Pavaizduokiet tokią informaciją: atrinktų butų kainų pasiskirstymą tarp miestų.
#pavaizduokite tokią informaciją - kiek buvo sklebimų per skirtingus miestus jūsų atrankoje?

Adresas = []
Kaina = []
Kaina_uz_m2 = []
Plotas = []
Kambariu_skaicius = []

for puslapis in range(2,12):
    url = f'https://www.aruodas.lt/butai/puslapis/{puslapis}/'
    driver.get(url)
    time.sleep(10)
    source = driver.page_source
    bs = BeautifulSoup(source, 'html.parser')
    ResultsSet = bs.find_all('div', {'class':'advert-flex'})

    for skelbimas in ResultsSet:
        try:
            addres_element  = skelbimas.find('div', {'class':'list-adress-v2'})
            tag = addres_element.find('h3').find('a', href=True)
            linkas = tag['href']
        # tekstą galima pasiekti ir per 
        # .contents atributą
            tekstas = tag.contents #jums gražina list objektą su teksto gabalais
            f = ''
            for i in tekstas:
                f = f + str(i).strip() # str - kad garantuotai būtų tekstas
            adresas = f.replace('<br/>', ', ')

            kainaRaw = addres_element.find('div', {'class':'price'}).find('span', {'class':'list-item-price-v2'})
            kainaFloat = float(kainaRaw.text.strip().replace(' ', '').replace('€', ''))
            
            kaina_uz_m2Raw = addres_element.find('div', {'class':'price'}).find('span', {'class':'price-pm-v2'})
            kaina_uz_m2Float = float(kaina_uz_m2Raw.text.replace('\n', '').replace(' ', '').replace('€/m²', ''))
            
            plotasRaw = skelbimas.find('div', {'class':'list-AreaOverall-v2'})
            plotasFloat = float(plotasRaw.text.strip().replace(' ', '').replace('m²', ''))

            kambariaiRaw = skelbimas.find('div', {'class':'list-RoomNum-v2'})
            kambariaiFloat = float(kambariaiRaw.text.strip().replace(' ', '').replace(' kamb.', ''))
            Kambariu_skaicius.append(kambariaiFloat)
            Adresas.append(adresas)
            Kaina.append(kainaFloat)
            Kaina_uz_m2.append(kaina_uz_m2Float)
            Plotas.append(plotasFloat)
        except:
            pass
    # time.sleep(np.random.randint(10,100))
    time.sleep(5)
driver.close()

dfVisiSkelbimai = pd.DataFrame(data={'Adresas':Adresas, 'Kaina':Kaina, 'Kaina_uz_m2':Kaina_uz_m2, 'Plotas':Plotas, 'Kambariu_skaicius':Kambariu_skaicius})

dfVisiSkelbimai.to_csv('20240423AruodasVisiSkelbimai.csv', sep=';')


