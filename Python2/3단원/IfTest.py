# 입력을 받을 것이다.
num = int(input())

#첫 번째 조건은 양수인지 확인하기
if num > 0:
    print("양수 입니다.")

#두 번째 조건을 넣고싶다. elif 사용합니다.
elif num < 0:
    print("음수 입니다.")
#모든 조건이 아닐 경우 실행하는 구문
else:
    print("0 입니다.")
