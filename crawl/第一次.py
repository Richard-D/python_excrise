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

def main():
    print(download(url))

if __name__ == "__main__":
    main()