try:
    num1 = int(input("첫 번째 정수를 입력하세요 : "))
    num2 = int(input("두 번째 정수를 입력하세요 : "))

    # 나눗셈 하는데 0을 나눴을 때 발생하는 오류
    print(f"num1 나누기 num2의 결과는 {num1 / num2} 입니다.")
    print("예외가 발생하면 여기는 실행되지 않습니다.")
# 0으로 나눗셉을 하면 발생하는 오류를 예외처리 하겠다.
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print("발생한 에러 : ", e)

# 잘못된 입력을 받았을 때 혹은 잘못된 값이 들어가서 발생하는 오류를 예외처리 하겠다.
except ValueError as e:
    print("숫자를 입력하세요.")
    print("발생한 에러 : ", e)

# finally : 예외 발생 여부와 상관없이 항상 실행해야 할 경우 사용
finally:
    print("finally는 예외가 발생하던 안 하던, 무조건 실행됩니다.")

