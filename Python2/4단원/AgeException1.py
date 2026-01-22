# 사용자 정의 예외 '클래스'
# 1. 상속을 받는다. = Exception
# 2. Exception이라는 부모에게 예외를 전달한다.
# 3. - super()를 통해서 전달을 하겠다.

#사용자 정의 예외 '클래스'이다.
class AgeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)


try:
    age = int(input("나이를 입력해주세요: "))
    if age < 1 or age > 200 :
        raise AgeError("사람의 나이는 1 이상 200 이하로 입력해주세요.")
    print(f"당신은 {age}살 이시군요!")

except Exception as e:
    print("예외 메시지 :",e)

finally:
    print("프로그램을 종료합니다.")