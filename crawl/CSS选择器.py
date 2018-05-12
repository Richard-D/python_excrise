from bs4 import BeautifulSoup
import requests

DOWNLOAD_URL = 'https://movie.douban.com/top250'

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url,headers = headers).content
    return data.decode("utf-8")
soup = BeautifulSoup(download_page(DOWNLOAD_URL),"html5lib")

title = soup.select("title")
print(title)

# 通过tag标签逐层查找
atag = soup.select("body a")
with open("atag.txt","w",encoding="utf-8") as ff:
    ff.write(str(atag))

# 找到某个tag标签下的子标签
childTag = soup.select("body > div")
print(childTag)