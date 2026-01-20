# 이터레이터
# - 한 번에 하나씩 값을 꺼낼 수 있는 객체를 의미
# - next() 함수를 통해 다음 값을 꺼내올 수 있음
# - 한 번 꺼내면 다시 꺼낼 수 없음
#   (map,filter도 이터레이터 객체로 반환을 해주는 것)

# 이터러블
# - 반복 가능한 객체를 의미
# - ex) 리스트, 튜플, 문자열 등 for문을 사용하여 거낼 수 있는 객체

numbers = [1, 2, 3]
it = iter(numbers) # 1, 2, 3이라는 값이 모두 들어가있는 이터레이터 객체로 변환
print(next(it)) # 1 출력
print(next(it)) # 2 출력
print(next(it)) # 3 출력
#print(next(it)) # 더이상 꺼낼 값이 없기 때문에 StopIteration 발생

str_list = ["Python", "AI", "BigData"]
it2 = iter(str_list)

for i in it2:
    print(i)

# 제너레이터
# - yield 키워드를 사용하여 값을 하나씩 반환하는 함수
# - 함수 호출 시점이 아니라 next()가 호출될 때 함수 실행
# - 메모리 효율성이 이터레이터에 비해서 좋음
#   (필요할 때만 메모리에 올리고 실행)

def gen():
    print("함수가 실행되었습니다!")# 4. 출력
    yield 10 # 5. 숫자 10을 반환, yield 키워드를 만나면서 함수 대기 상태로 돌입
    print("A") # 9. 출력
    yield 20 # 10. 숫자 20을 반환, yield 키워드를 만나면서 함수 대기 상태로 돌입
    print("B")# 14. 출력
    yield 30# 15. 숫자 30을 반환, yield 키워드를 만나면서 함수 대기 상태로 돌입
    print("C") # 19. 출력

result = gen() # 1. 메모리에 함수 올리기 (제너레이터 객체를 저장)
print("첫번째 next실행") # 2. 가장 먼저 실행
print(next(result)) # 3. next()가 호출되면서 함수 실행
#6. 10을 반환 받아서 10 출력 -> print(10)

print("두번째 next실행") # 7. 출력
print(next(result)) # 8. next()가 호출되면서 함수 호출(실행 상태로 돌입)
# 11. 20을 반환 받아서 20 출력 -> print(20)

print("세번째 next실행") # 12. 출력
print(next(result)) # 13. next()가 호출되면서 함수 호출(실행 상태로 돌입)
#16. 30을 반환 받아서 30 출력 -> print(30)

print("네번째 next실행")# 17. 출력
print(next(result))#18. next()가 호출되면서 함수 호출(실행 상태로 돌입)
# 20. 더이상 꺼낼 yield 키워드가 없기 때문에 StopIteration 발생

def squares(num):
    i = 0 # 3. i = 0 , num = 3
    while i < num: # 4. 0 < 4 True while 실행 #9 14
        yield i*i # 5. 0 * 0 = 0 / 숫자 0 을 반환 #10 15
        i += 1 # 8 13

result = squares(3)# 1. 메모리에 함수 올리기
print(next(result)) # 2. next()가 호출되면서 함수 실행 #6

print(next(result))# 7 # 11
print(next(result)) #12 16
#print(next(result)) #yield 키워드를 만나지 못했기 때9문에 StopInteration 발생

# 1. 1부터 N가지 출력하는제너레이터:
def gen_numbers(n):
    for i in range(1,n+1):
        yield i

input = int(input("숫자 입력 : "))

# 1. for문이 내부적으로 gen_numbers(3) 을 제너레이터 객체로 반환
# 2. 내부적으로 next()를 호출해서 반환된 값을 number 변수에 할당
for number in gen_numbers(input):
    print(number)

# 1. [1, 2, 3] 리스트를 이터레이터 객체로 변환
#    result = iter([1, 2, 3])
# 2. next(result) 호출
# 3. i = 1
#    i = next(result)
# 4. print(i)니까 1 출력
# 5. next(result) 호출
# 6. i = 2
# 7. print(i) 니까 2 출력
# 8. next(result) 호출
# 9. i = 3
# 10. print(i)니까 3 출력
# 11. next(result) 호출 -> StopIteration 발생 -> for문 종료
for i in [1,2,3]:
    print(i)

def for_def(n):
    iter_obj = iter(n) # 이터레이터 변환

    while True:
        i = next(iter_obj) # next() 계속 호출
        print(i)

# 2. 제너레이터로 range() 구현 해보기
def range_def(start, end):
    while start < end:
        yield start
        start += 1

#list
# result = []
# while True:
# result.append(next(range_def))

print(list(range_def(1,6))) # list(range(1,6))
