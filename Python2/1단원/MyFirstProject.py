# 사람이라는 설계도를 작성
class Person:
    def __init__(self,name): # 생성자 선언
        self.name = name

    # introduce는 행동이다. 동작하는 것이다.(함수)
    def introduce(self):
        # self.name = name # 멤버변수 : class 안에서 사용하는 변수
        print(f"안녕하세요 제 이름은 {self.name} 입니다.")

# Person이라는 설계도(Class)를 사용할 것이다.
# 이름은 a라고 명시하겠다.

a = Person("민수") # 생성자 호출
a.introduce()

print(a.name)
#
# b = Person("Tom")
# b.introduce()
#
