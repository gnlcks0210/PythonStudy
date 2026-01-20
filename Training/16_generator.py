# Q1. 아래의 코드에서 주석으로 실행 순서를 작성하시오.
def gen_chars(text):
    for ch in text: #3 7 11 14
        yield ch # 4 8 15


q1 = gen_chars('CSS') # 1
print(next(q1)) # 2 5
print(next(q1))#6 9
print(next(q1))# 10 12
#print(next(q1))# 13 -> StopIteration에러

# Q2. 짝수만 반환하는 제너레이터
# - 1부터 N까지
# - 출력 방식은 하나씩도 가능, 리스트로 한번에 출력도 가능
def q2_gen_even(num):
    for n in range(1,num+1):
        if n % 2 == 0:
            yield n

print(list(q2_gen_even(10)))

# Q3. 아래의 리스트에서 각 문자열의 길이를 반환하는 제너레이터
q3_words = ["apple", "banana", "kiwi"]
def q3_gen_length(words):
    for word in words:
        yield len(word)

print(list(q3_gen_length(q3_words)))

# Q4. 아래의 리스트에서 합계를 반환하는 제너레이터
q4_numbers = [10, 30, 50, 80]
def q4_gen_sum(numbers):
    yield sum(numbers)

print(list(q4_gen_sum(q4_numbers)))

# Q5. 아래의 리스트에서 문자열 ERROR가 포함된 로그만 출력
logs = [
    "INFO 서버가 시작되었습니다.",
    "ERROR 데이터베이스 연결 실패",
    "INFO 유저가 로그인하였습니다.",
    "ERROR 시간 초과"
]
def q5_gen_error_log(logs):
    for log in logs:
        if "ERROR" in log:
            yield log
print(list(q5_gen_error_log(logs)))

# Q6. 매출 데이터 중 가격이 150,000원 이상인 데이터만 하나씩 출력

sales_data = [
    {"item": "마우스","price":13000},
    {"item": "데스크탑","price":750000},
    {"item": "키보드","price":36000},
    {"item": "모니터","price":230000},
]
def q6_gen_sales_filter(sales_data):
    for data in sales_data:
        if data["price"] >= 150000:
            yield data

for d in q6_gen_sales_filter(sales_data):
    print(d)