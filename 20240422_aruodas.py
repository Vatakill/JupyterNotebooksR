#!/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

opcijos = Options()
opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless')

driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)


url = "https://www.aruodas.lt/butai/puslapis/2/"

driver.get(url)

time.sleep(30)

source = driver.page_source

bs = BeautifulSoup(source, 'html.parser')
ResultsSet = bs.find_all('div', {'class':'advert-flex'})
print(len(ResultsSet))

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
        kainaInt = kainaRaw.text.strip().replace(' ', '').replace('€', '')
        kainaInt = int(kainaInt)

        kaina_uz_m2Raw = addres_element.find('div', {'class':'price'}).find('span', {'class':'price-pm-v2'})
        kaina_uz_m2Int = kaina_uz_m2Raw.text.replace('\n', '').replace(' ', '').replace('€/m²', '')
        kaina_uz_m2Int = int(kaina_uz_m2Int)

        # tuo tarpu .text gražina contents tekstą kaip vientisą
        # tekstas = tag.text.strip() # string metodas, skirtas pašalinti tarpus iš pradžios bei pabaigos
        print("====SKELBIMAS====")
        print(linkas, adresas, 'Kaina', kainaInt, 'Kaina uz m2', kaina_uz_m2Int, sep="\n")
    except:
        pass

#     Jūsų užduotis:
# Iš printinti linką, adresą, buto kainą, buto kainą už 1 kv metrą, vaizdas turi būti toks:
# ===SKELBIMAS===
# linkoas,
# adreas
# kaina
# kaina už 1 kv metrą

driver.close()