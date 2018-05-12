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

print(soup.name)
print(soup.a)
print(soup.a["href"])
print("================")
print(soup.a.string)

# 注释
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,"html5lib")
comment = soup.b.string
cdata = CData("A CDATA block")
comment.replace_with(cdata)
print(soup.b.prettify())