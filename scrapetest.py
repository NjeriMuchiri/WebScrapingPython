from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
   html = urlopen("http://pythonscraping.com/pages/page3.html")
   bs = BeautifulSoup(html.read(), 'html.parser')
   print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
   """ for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
        print(sibling) """                         
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found")
else:
    print(bs.h1.prettify())

