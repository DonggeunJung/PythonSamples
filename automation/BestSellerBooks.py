import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=09'
res = requests.get(url)
html = res.content
book = bs(html, 'html.parser')
# print(book)

best = pd.DataFrame(columns=['Book', 'Authod', 'Price', 'URL'])
for index, book_info in enumerate(book.select('td.goodsTxtInfo')) :
    book_title = book_info.select_one('a').text.strip()
    book_author = book_info.select_one('div.aupu > a').text.strip()
    book_price = book_info.select_one('span.priceB').text.strip()
    book_url = book_info.select_one('a').attrs['href']
    # print(book_title, book_author, book_price, book_url)
    best.loc[index+1] = (book_title, book_author, book_price, book_url)

best.to_excel('bestseller.xlsx')
