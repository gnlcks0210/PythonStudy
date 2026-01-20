# class를 선언
# 부모
class Parent:
    def __init__(self,name):
        print("생성자 실행완료")
        self.name = name

    def hello(self):
        # print(f"안녕하세요. 부모클래스의 hello입니다. 저의 이름은 {self.name}입니다.")
        print("안녕하세요. 부모클래스의 hello입니다. 저의 이름은",self.name,"입니다.")

# 자식
class Child(Parent):
    def __init__(self,name,age):
        print("Child의 생성자 입니다.")
        super().__init__(name)
        print("super() 실행완료")
        self.age = age

    def bye(self):
        print(f"안녕히가세요. 자식클래스의 bye 입니다. 저의 이름은 {self.name}이며 나이는 {self.age} 입니다.")
# ********************************************************
child = Child("홍길동",20)

child.hello()
child.bye()



