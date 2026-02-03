# urllib는 Python 기본 라이브러리이다. ( 웹 크롤링 )
# request는 urllib 안에 있는 하위 모듈로 웹 서버에게 요청(request)을 보내는 기능이다.
#urlopen : request 모듈 안에 있는 함수로 특정 URL에 접속해서 웹 데이터를 가져온다.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import certifi
#
# # 1. 크롤링할 웹 사이트 주소를 변수에 저장
# # url = "https://quotes.toscrape.com"
# #url = "http://www.naver.com"
#
# # urlopen(url) : 해당 URL에 접속하여 서버의 응답을 받는다.
# # .read() : 응답받은 데이터를 전부 읽는다.
# context = ssl.create_default_context(cafile=certifi.where())
# html = urlopen(url, context=context).read()
#
# print(html)

#****************************************************************************************

# 2. beautifulSoup

url = "https://quotes.toscrape.com"
context = ssl.create_default_context(cafile=certifi.where())
html = urlopen(url, context=context).read()

# BeautifulSoup를 사용해서 파싱하고 원하는 데이터 가져오기
soup = BeautifulSoup(html, features="html.parser")
# -> 가져온 HTML을 파싱한다. ( 트리 구조로 바꾼다.)

# soup의 find함수를 이용해서 원하는 태그를 가져올 수 있다.
# title이라는 변수에 h1 태그를 가져오겠다.

# h1이라는 태그를 찾는다.
# get_text를 이용해서 찾은 태그 안에서 텍스트를 가져오겠다.
# ex) <a>Login</a> 이런식의 태그가 잇다면 Login이라는 글자를 가져온다.
# ex) <h1>안녕하세요</h1> 안녕하세요라는 텍스트를 가져온다.
# title = soup.find("h1").get_text()
#
# print("페이지 제목: ", title)


#****************************************************************************************

# find 사용

# # div : 웹 페이지에 여러 요소를 하나로 묶어주는 영역(상자)
# #       화면을 각 구역별로 나누기 위해서 사용하는 상자
# frist_quote = soup.find("div",class_ = "quote")
#
# # prettify() : 들여쓰기
# # 사람이 조금 더 쉽게 확인 할 수 있도록
# print(frist_quote.prettify())

#****************************************************************************************

#find_all

# # div 태그를 가져올 것이고, 클래스가 quote라는 것을 가져온다.
# all_quotes = soup.find_all(name = "div",class_="quote")
# #print(all_quotes)
# # 배열로 가져오기
# print(all_quotes[1])

#****************************************************************************************

# get_text() 사용해서 요소의 텍스만 출력

#soup.find_all()
# all_quotes = soup.find_all(name = "div", class_ = "quote")
# text = all_quotes[1].find("span",class_ = "text").get_text()
# print(text)
# 태그 안에 텍스트만 가져오겠다. -> get_text()를 사용

#****************************************************************************************

# attrs
# 특정 속성만 가져오기
# frist_div = soup.find("div")
# # print(frist_div)
# # 첫 번째로 만나는 div의 class를 가져와라
# # 속성을 딕셔너리 형태로 출력
# print(frist_div.attrs)
# print(frist_div["class"])

# urlopen 사용
# -> request를 생성해서 웹 페이지에 접속하여 데이터를 모두 가져온다.(HTML)

# BeautifulSoup
# ->urlopen을 통해서 가져온 데이터를 파싱한다.

#**********************************
#실습

# find_all을 사용하고 3번쨰 인덱스에 있는 quote라는 내용을 찾는다.
# find를 이용해서 a태그를 가져온다.
# a태그의 텍스트를 가져온다.

all_quotes = soup.find_all("div",class_="quote")
text = all_quotes[3].find("a").get_text()
print(text)



