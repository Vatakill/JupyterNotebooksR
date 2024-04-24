import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import selenium
# import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


opcijos = Options()
opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless')

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

data = []
url = "https://m.autoplius.lt/skelbimai/naudoti-automobiliai?qt=&page_nr={}"

for pgnr in range(1,5):
    urlf = url.format(pgnr)
    driver.get(urlf)
    time.sleep(45)
    src = driver.page_source
    bs = BeautifulSoup(src, 'html.parser')
    skelbimai = bs.find_all('div', {'class':'description'})
    try:
        for skelbimas in skelbimai:
            year = skelbimas.find('div', {'class':'title-year'}).text.strip()
            gm = skelbimas.find('div', {'class':'line1'}).text.strip()
            kaina = skelbimas.find('div', {'class':'pricing-container'}).find('strong').text.strip()
            parametrai = skelbimas.find('div', {'class':'item-parameters'}).text.strip().replace('\n\n','\n').replace('\n',';').replace('  ','')
            pars = parametrai.split(';')
            vieta = pars[-1]
            tipas = pars[-2]
            rida = 'Nenurodyta'
            if 'km' in parametrai:
                rida = pars[-3]
            pavaros=pars[-4]
            variklis = 'Nenurodyta'
            kuras = pars[0]
            if 'kW' in parametrai:
                variklis = pars[-5]                
            print("====SKELBIMAS===")
            print(pars)
            d = {'gm':gm,'year':year,'kaina':kaina,'rida':rida,'pavaros':pavaros,'kuras':kuras,'variklis':variklis}
            data.append(d)
    except Exception as ex:
        pass

df = pd.DataFrame(data=data)
df.to_csv('mobile_autoplius.csv', sep=';')          