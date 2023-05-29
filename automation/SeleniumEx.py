import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


URL = 'https://www.naver.com'
driver = webdriver.Chrome('chromedriver_mac_arm64.zip')
driver.get(URL)
#print(driver.current_url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# tag_list = soup.select(('body p')) # get <p> tag in <body>
# for tag in tag_list :
#     print(tag.text)
# btn = driver.find_element(By.XPATH, '//*[@id="account"]/div/a')
# btn.click()
input_tag = driver.find_element(By.CSS_SELECTOR, '#query')
input_tag.send_keys('방탄소년단')
input_tag.send_keys('\n')
driver.implicitly_wait(3)
driver.close()
