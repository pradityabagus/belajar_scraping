from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_887473.html"
page = urlopen(url,context=ctx).read()

souped = bs(page,"html.parser")
linktag = souped.find_all('span', class_='comments')

sum = 0

for link in linktag:
    sum += int(link.contents[0])

print(sum)
