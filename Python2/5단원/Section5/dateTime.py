import datetime

# 첫 번째 datetime은 모듈명 이다.
# 두 번째 datetime은 클래스명 이다.
# 세 번쨰 현재 날짜와 시간을 가져오는 함수이다.
persent = datetime.datetime.now()
print(f"현재 날짜 및 시간 : {persent}")

# 날짜만 출력
print(f"오늘 날짜는 {persent.date()}")

# 년도만 출력
print(f"지금은 {persent.year}년 입니다.")
print()

birthday = datetime.date(year = 2002, month = 12, day = 31)
print("YYYY-MM-DD 패턴으로 변환된 결과는 :",birthday)
