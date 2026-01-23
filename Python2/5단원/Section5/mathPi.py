# # 수학에 관련된 파이썬 내장 모듈
import math

# ceil, floor, trunc 사용

# ceil : 소수점을 올림 처리하는 함수
print(f"1.2를 올림 처리하면 {math.ceil(1.2)}")
print(f"3.5를 올림 처리하면 {math.ceil(3.5)}")

# floor : 소수점을 내림 처리하는 함수
print(f"1.7를 내림 처리하면 {math.floor(1.7)}")
print(f"2.7를 내림 처리하면 {math.floor(2.7)}")

# trunc : 소수점을 버리는 함수
print(f"1.3의 소수점 이하를 버리면 {math.trunc(1.3)}")
print(f"2.3의 소수점 이하를 버리면 {math.trunc(2.3)}")

# sqrt : 제곱근을 하는 함수이다.
print(f"4를 제곱근하면 {math.sqrt(4)}")

# pow : 거듭제곱을 하는 함수이다.
print(f"2를 3번 거듭제곱 하면 {math.pow(2,3)}")

# ******************************************************

#round(파이썬 내장 함수) : 값을 반올림 해주는 함수
print(f"8.2를 반올림 처리하면 {round(8.2)}")
print(f"4.6를 반올림 처리하면 {round(4.6)}")




#
# #원의 반지름을 입력하면 원의 둘레를 구해주는 함수
#
# def calc_circumference(radius):
#     return 2 * math.pi * radius
#
# radius = float(input("반지름의 값을 입력해주세요 : \n"))
# result = calc_circumference(radius)
# print(f"입력하신 원의 둘레는 {result} 입니다.")
