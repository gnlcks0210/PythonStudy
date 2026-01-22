try:
    num1 = int(input("첫 번째 정수를 입력하세요 : "))
    num2 = int(input("두 번째 정수를 입력하세요 : "))

    #나눗셈 하는데 0을 나눴을 때 발생하는 오류
    print(f"num1 나누기 num2의 결과는 {num1/num2} 입니다.")

# 0으로 나눗셉을 하면 발생하는 오류를 예외처리 하겠다.
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print("발생한 에러 : ", e)

#잘못된 입력을 받았을 때 혹은 잘못된 값이 들어가서 발생하는 오류를 예외처리 하겠다.
except ValueError as e:
    print("숫자를 입력하세요.")
    print("발생한 에러 : ", e)

# Exception은 모 예외의 최상위로 어떤 오류가 오더라도 전부 처리한다.
# 장점 : 일일이 오류를 입력하지 않아도 된다.
# 단점 : 어떤 오류가 발생했는지 정확하게 모른다.
except Exception:
    print("오류발생")

