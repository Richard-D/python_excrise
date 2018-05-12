# from bs4 import BeautifulSoup
# import requests
# import urllib.request as up
#
# DOWNLOAD_URL = 'http://example.webscraping.com'
#
# def download_page(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
#     }
#     data = requests.get(url,headers = headers).content
#     return data.decode("utf-8")
#
# import re
#
# def link_crawler(send_url,link_regex):
#     crawl_queue = [send_url]
#     while crawl_queue:
#         url = crawl_queue.pop()
#         html = download_page(url)
#         for link in get_link(html):
#             if re.match(link_regex,link):
#                 link = up.urljoin(send_url,link)
#                 crawl_queue.append(link)
#     print(crawl_queue)
#
# def get_link(html):
#     webpage_regex = re.compile("<a[^>]+href=['\"](.*?)['\"]",re.IGNORECASE)
#     return webpage_regex.findall(html)
#
# def main():
#     link_crawler('http://example.webscraping.com', '/(index|view)')
#
# if __name__ == "__main__":
#     main()

import re
import urllib.request as ur

def download(url,num_retries = 2):
    try:
        html = ur.urlopen(url).read().decode("utf-8")
        return html
    except:
        html = None
        if  num_retries>2:
            return download(url,num_retries-1)

def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url] # the queue of URL's to download
    while crawl_queue:
        url = crawl_queue.pop()
        seen = set(crawl_queue)
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                link = ur.urlparse()
                # add this link to the crawl queue
                if link not in seen:
                    crawl_queue.append(link)
    print(crawl_queue)


def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(index|view)')
