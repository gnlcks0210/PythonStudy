class Calculator:
    def __init__(self,value =0):
        self.__value = value

    # 기존에 property (getter, setter)
    # 1. 멤버변수를 비공개로 바꿔주기
    # 2. getter 메소드 선언하기
    @property
    def value(self):
        return self.__value
    # 3. setter 를 선언하기
    @value.setter
    def value(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError("숫자만 입력이 가능합니다.")
        self.__value = value

    def add(self,x):
        self.__value += x

    def sub(self,x):
        self.__value -= x

    def mul(self,x):
        self.__value *= x

    def div(self,x):
        if x == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        self.__value /= x


#     def reset(self):
#         self.__value = 0
#
# # 1. Calculator 선언하기
# cal = Calculator()
#
# # 2. add 메소드를 사용하여 10을 더하고 출력하기
# cal.add(10)
# print(cal.value)
#
# # 3. sub 메소드를 사용하여 2를 빼고 출력하기
# cal.sub(2)
# print(cal.value)
#
# cal.reset()
# print(cal.value)

calc = Calculator()

#초기값 입력
# num = int(input("초기 값을 입력하세요 : "))
# calc.value = num
calc.value = int(input("초기 값을 입력하세요 : "))


op = input("연산을 선택하세요 ( +, - , * , / ) : ")
x = int(input("계산할 숫자를 입력하세요 : "))

if op == "+":
    calc.add(x)
elif op == "-":
    calc.sub(x)
elif op == "*":
    calc.mul(x)
elif op == "/":
    calc.div(x)
else:
    print("잘못된 연산자입니다.")

print("결과", calc.value)
