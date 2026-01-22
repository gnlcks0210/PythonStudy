num1 = input("첫 번째 정수를 입력하세요 : ")
num2 = input("두 번째 정수를 입력하세요 : ")

# 2개의 변수를 선언하고 초기화했다.


if num1 == "0" or num2 == "0":
    print("0으로 나눌 수 없습니다.")
elif not num1.isdigit() or not num2.isdigit():
    print("문자는 입력할 수 없습니다.")
else:
    #result에서  num1과 num2를 형벼환해주고, 나눗셈을 해준다.
    result = int(num1) / int(num2)
    print(f"num1 나누기 num2의 결과는 {result}입니다.")
#num1 과 num2를 나눗셈하는 것을 출력해준다.