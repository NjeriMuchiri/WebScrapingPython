from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.om/pages/page1.html')
bs = BeautifulSoup(html.read(), 'lxml')
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())