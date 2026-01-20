#<연산자>
# - 수학적 계산이나 데이터 처리를 수행하기 위해 사용하는 기호 또는 기호 조합

#<산술 연산자>
# - 기본적인 수학적 계산을 수행 (사칙 연산)
num_1 = 100
num_2 = 3

add = num_1 + num_2
print("덧셈 결과 : ", add)

#변수명 : sub
#빼기를 수행하는 기호 : -
sub = num_1 - num_2
print("뺄셈 결과 : ", sub)
mul = num_1 * num_2

#변수명 : mul
#곱셈을 수행하는 기호 : *
mul = num_1 * num_2
print("곱셈 결과 : ", mul)

#변수명 : div
#나눗셈을 수행하는 기호 : /(소수점 포함), //(몫 , 소수점 버림) ,%(나머지)
div = num_1 / num_2
print("나눗셈 결과 : ", div)

div_2 = num_1 // num_2
print("나눗셈 결과 : ", div_2)

div_3 = num_1 % num_2
print("나눗셈 결과 : ", div_3)

# 짝수 구하기
num_3 = 22
is_even = num_3 % 2 == 0
# 1. 22 % 2 == 0
# 2. 0 == 0
# -22 나누기 2의 결과(나머지) 는 0
# -0과 0이 일치하냐? -> 일치하기 때문에 True
print("num_3 % 2의 결과 : ",is_even)

#<대입(할당) 연산자>
# - 변수에 값을 할당할 때 사용하는 연산자
# - 일반적으로 대입 연산자라고 많이 부름
num_4 = 23

#<복합 대입 연산자>
# - 사칙 연산을 더 짧고 쉽게 사용할 수 있도록 해주는 연산자
num_5 = 50
num_6 = 77
# num_5 = num_5 + num_6 # 결과: 127, 기존 방식 ( 산술연산자 )
# print("num_5 : ", num5)

num_5 += num_6 # 복합 대입 연산자 num_5+num_6 실행한 결과가 다시 num_5에 저장 된다.
print("num5 : ", num_5) # 결과: 127

#<비교 연산자>
# - 두 개의 값을 비교하여 그 결과가 참(True)인지 거짓(False) 판별하는 연산자

#<비교 연산자 종류>
# 1. a  > b / a 가 b보다 크다
# 2. a >= b / a 가 b보다 크거나 같다
# 3. a < b  / a 가 b보다 작다
# 4. a <= b / a 가 b보다 작거나 같다
# 5. a == b / a 와 b는 같다
# 6. a != b / a 와 b는 같지 않다

print("10 > 5 : ",10 > 5) # 10이 5 보다 크기 때문에 True
print("10 <= 10 : ", 10 <= 10) # True
print("33 != 27 : ",33 != 27) # True

num_7 = 100
num_8 = 101

#변수명 : is_equals
# - num_7과 num_8이 같은지 비교하여 출력
is_equals = num_7 == num_8
print("num_7 == num_8 : ",is_equals)

str_one = "1" #문자
int_one = 1 # 숫자

print("str_one == int_one : ",str_one == int_one)

#논리 연산자
# - 논리적인 연산을 수행하여 참(True)인지 거짓(False)인지 판단하는 연산자
# - 종류 and, or, not

is_snowing = True
is_cold = True

# and : 양쪽의 값이 모두 True일 때 True 반환
#       하나라도 False이면 False 반환
# is_snowing과 is_cold가 둘 다 True라면 최종적으로 True 반환
is_winter = is_snowing and is_cold
print("is_snowing : ",is_snowing)

age = 15
height = 162
# 놀이공원의 입장 조건이 나이 13세 이상, 키 150 이상
is_join = age >= 13 and height >= 150

# 1. True and height >= 150
# 2. True and True
# 3. and 연산 후 최종적으로 True 반환
print("is_join : ",is_join)

#-------------------------
is_snowing = True
is_cold = False

# or 연산자 : 둘 중 하나라도 True가 있으면 최종적으로 True 반환
is_winter = is_snowing or is_cold
print("is_snowing : ",is_snowing)

price = 60000 #구매 금액
is_member = False # 비회원

#구매 금액이 50,000원 이상 이거나 회원이라면 True
result = price >= 50000 or is_member
print("result : ",result)

#not 연산자 : True면 False로 반환, False면 True로 반환
is_ture = True
is_not_ture = not is_ture

print("is_not_ture : ",is_not_ture)

# 조건 연산자
# - 조건에 따라서 결과를 선택할 수 있음
num_1 = 25
num_2 = 23

#더 큰 값을 변수에 할당
max = num_1 if num_1 > num_2 else num_2
print("max : ",max)


# 비트 연산자
# - 숫자를 2진수로 변환하여 비트 단위 연산을 수행

#컴퓨터는 0과 1만 알고 있음
# - 이 숫자(0 or 1) 하나를 비트(bit)라고 부름

#비트가 8개 있으면(8bit) 1바이트(1byte)라고 부름

#시프트 연산자(<<, >>)
# - 비트를 왼쪽 또는 오른쪽으로 밀어줌
x = 5 #2진수로 바꾸면 0101
print(x << 1)   # 1 0 1 0
print(x << 2)   # 1 0 1 0 0

# 2진수 : 0   1   1   0   1   0   1   0
#       128  64  32  16  8   4   2   1
#       ------------------------------
# 10진수 :                          106