class Parent:
    def hello(self):
        print("부모 클래스의 hello 입니다.")

class Child(Parent):
    def hello(self):
        print("자식 클래스의 hello 입니다.")

    def bye(self):
        print("자식 클래스의 bye 입니다.")

def greet(person):
    person.hello()

c = Child()
greet(c)

p = Parent()
greet(p)