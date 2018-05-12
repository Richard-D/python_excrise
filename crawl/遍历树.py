from bs4 import BeautifulSoup
import requests
from bs4 import CData

DOWNLOAD_URL = 'https://movie.douban.com/top250'

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url,headers = headers).content
    return data.decode("utf-8")
soup = BeautifulSoup(download_page(DOWNLOAD_URL),"html5lib")

atag =  soup.find_all("a")
# print(atag)

headtag = soup.head
print(headtag.contents[1])
print(soup.contents[1].name)

# for child in soup.children:
#     print(child)

for string in soup.stripped_strings:
    print(repr(string))

