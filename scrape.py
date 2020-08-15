from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_42.html"
page = urlopen(url,context=ctx).read()

souped = bs(page,"html.parser")
linktag = souped.selec

for link in linktag:
    print(link)
