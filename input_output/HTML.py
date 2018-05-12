import requests

url = "http://lxml.de/tutorial.html#parsing-from-strings-and-files"

resp = requests.get(url)
print(resp)