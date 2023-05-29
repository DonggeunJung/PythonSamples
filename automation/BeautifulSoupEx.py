from bs4 import BeautifulSoup

# html_txt = """<p class = 'weather' id = 'tw'>Today weather</p>\
#            <h1>It will be shower from time to time</h1>"""
#
# soup = BeautifulSoup(html_txt, 'html.parser')
# tag = soup.find('p') # find <p> tag
#
# print(tag)
# print(tag.name)
# print(tag.attrs)
# print(tag.attrs['class'])
# print(tag.attrs['id'])
# print(tag.text)

html_txt = """
    <html>
    <head><title>BS page</title></head>
    <body>

    <h1 class='portal_cls'>Search potal</h1>
    <p>
    <a href='http://www.daum.net'>Daum link</a><br>
    "<a href='http://www.naver.com'>Naver link</a>
    </p>
    <a href='http://www.google.com' class='alink_cls'>Google</a>
    <p class='footage_cls' id='company'>2021, ABC Company </p>
    <p class='footage_cls' id='addr'>Korea</p>
    </body>
    </html>
"""
soup = BeautifulSoup(html_txt, 'html.parser')
# tag = soup.select_one('h1')
# print(tag.text)

# tag_list = soup.select('h1')
# tag_list = soup.select('body p > a') # find <a> tag in <body><p>
# tag_list = soup.select('.footage_cls') # find tag by class name
tag_list = soup.select('#company') # find tag by ID
for tag in tag_list :
    print(tag.text)
