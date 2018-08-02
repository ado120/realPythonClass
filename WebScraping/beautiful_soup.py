from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

my_address = "https://realpython.com/practice/dionysus.html"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
html_page = Request(my_address, headers=headers)
html_text = urlopen(html_page).read()

my_soup = BeautifulSoup(html_text)

print(my_soup.get_text())