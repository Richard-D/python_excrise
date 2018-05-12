import urllib.request
import urllib.error

url = "http://example.webscraping.com"

def download(url,num_retries = 2):
    try:
        html = urllib.request.urlopen(url).read().decode("utf-8")
        return html
    except:
        html = None
        if  num_retries>2:
            return download(url,num_retries-1)

import itertools

def iterway(url):
    max_error = 5
    num_error = 0
    num = 0
    for page in itertools.count(3):
        num += 1
        url = url+"/places/default/view/Afghanistan-%d" %page
        print(url)
        html = download(url)
        if html is None:
            num_error += 1
        if num_error == max_error:
            break
        else:
            num_error = 0
    return html,num

import re

def link_crawler(send_url, link_regex):
    crawl_queue = [send_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                link = urllib.request.urljoin(send_url,link)
                crawl_queue.append(link)

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)


def main():
    print(iterway(url))

if __name__ == "__main__":
    main()