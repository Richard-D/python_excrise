import urllib.robotparser as urp

rp = urp.RobotFileParser()
rp.set_url("http://example.webscraping.com/robots.txt")
print(rp.read())
url = "http://example.webscraping.com/"
user_agent = "BadCrawler"
a = rp.can_fetch(useragent=user_agent,url=url)
print(a)