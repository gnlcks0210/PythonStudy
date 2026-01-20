# for문
#  - 반복할 횟수를 알고 있는 경우에 사용
#  - 일반적인 상황에서 주로 사용

# 문법
#  for 변수명 in 리스트:
#    실행할 코드
# numbers = [1, 2, 3, 4, 5]
numbers = [1, 5, 100, 200, 500]
print(numbers)

for number in numbers:
    print(number)

# 문자열도 반복 가능
str = "Hello, World!"

for ch in str:
    print(ch)

# 1부터 5까지의 합을 구하는 코드
numbers = [1, 2, 3, 4, 5]
sum = 0 # 합계

for number in numbers:
    sum = sum + number
    # <반복이 처음 돌 때>
    #  sum = 0
    #  number = 1
    #  sum = 0 + 1  ->  1 할당

    # <반복이 두번째로 돌 때>
    # sum = 1
    # number = 2
    # sum = 1 + 2   ->  3 할당
print(f"합계 : {sum}")

# range() : 특정 길이를 가진 리스트를 생성
# range(100) : 0부터 99까지
# range(1, 101) : 1부터 100까지
sum = 0

for number in range(1, 101):
    sum = sum + number

print(f"합계 : {sum}")

# 구구단(2단)
#  - range()를 사용
#  - 출력 : 2 * 1 = 2    2 * 2 = 4    ...
for number in range(1, 10):
    print(f"2 * {number} = {2*number}")

# 중첩 for문
#  - for문안에 for문이 더 있는 구조
str_list = ["A", "B", "C"]
number_list = [1, 2, 3]

for str in str_list:
    print(f"처음 for문 도는중 값은 {str}")

    for number in number_list:
        print(f"안쪽 for문 도는중 값은 {number}")

    print("--------------------")

# 구구단 (2단 ~ 9단)
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")






