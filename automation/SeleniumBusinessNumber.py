from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome('chromedriver_mac_arm64.zip')
url = 'https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml'
driver.get(url)
time.sleep(3)

resultList = []
df = pd.read_excel('./docs/business_number.xlsx')
# print(df)

for regNo in df['Business_no'] :
    driver.find_element(By.CSS_SELECTOR, '#bsno').send_keys(regNo)
    driver.find_element(By.CSS_SELECTOR, '#trigger5').click()

    time.sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, '#grid2_cell_0_1').text
    resultList.append(result)
    #print(result)

df['result'] = resultList
df.to_excel('business_number_result.xlsx')
driver.close()
