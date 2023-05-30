from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

URL = 'https://finance.naver.com/marketindex'
driver = webdriver.Chrome('chromedriver_mac_arm64.zip')
driver.get(URL)
driver.switch_to.frame('frame_ex1')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
result = []
currency = soup.select('body > div > table > tbody > tr')

for data in currency :
    country = data.select('td.tit > a')[0].text.strip()
    exchange = data.select('td.sale')[0].text.strip()
    result.append([country, exchange])

#print(result)
df = pd.DataFrame(result, columns=['Currency', 'Exchange rate'])
df.to_csv('exchange_rate.csv', encoding='utf-16', header=True, index=False)
driver.close()
