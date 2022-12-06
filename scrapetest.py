from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
   html = urlopen("http://pythonscraping.com/pages/page1.html")
   bs = BeautifulSoup(html.read(), 'html.parser')
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found")
else:
    print(bs.h1)

