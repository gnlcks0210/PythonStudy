import scrapy

#QuotesSpider라는 나만의 스파이더 파일(Class)을(를) 생성한다.
class QuotesSpider(scrapy.Spider):
    # 터미널에서 실행할 Spider의 이름을 "quotes"라고 명시한다.
    # 실행 명령어 : scrapy crawl quotes ...
    name = "quotes"

    # 이 도메인 안에서만 크롤링을 하도록 허용하겠다.
    allowed_domains = ["quotes.toscrape.com"]

    # 크롤링을 시작할 첫 페이지의 주소
    start_urls = ["https://quotes.toscrape.com"]

    # parse라는 함수를 만듦
    # response에는 웹 페이지 HTML 전체가 들어가있다. [response : 매개변수]
    def parse(self, response):
        #페이지 에서 div.quote요소들을 전부 반복처리
        for quote in response.css("div.quote"):
            # span.text 요소들을 가져온다. ( 명언 텍스트 부분을 가져오겠다. )
            # ::text : 실제 글자만 가져옴
            # get(): 첫 번째 값 반환
            # (1) 명언을 가져오기
            text = quote.css("span.text::text").get()
            # (2) 명언의 작성자의 이름을 가져오기
            author = quote.css("small.author::text").get()
            # Scrapy에게 " 이 데이터를 저장해" 라고 전달한다.
            # 추출한 데이터는 딕셔너리 형태로 저장
            yield {
                "text" : text,
                "author" : author,
            }

