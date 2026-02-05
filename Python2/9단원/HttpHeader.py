#urlopen과 BeautifulSoup를 import
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl
import certifi

url = "https://quotes.toscrape.com"
context = ssl.create_default_context(cafile=certifi.where())

#header
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyPythonApp/1.0)",
    "Accept-Language":"ko-KR, en;q=0.9"
}

req = Request(url, headers=headers)

html = urlopen(req,context = context).read()

soup = BeautifulSoup(html, "html.parser")

#find를 통해서 첫 번째로 만나는 div와 그 자식을 가져오도록 하겟다.
first_div = soup.find("div")
print(first_div)
print(first_div["class"])