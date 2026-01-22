# class Person:
#     #생성자를 만들기
#     def __init__(self,name):
#         self.name = name
#     #__str__ 메서드 : 객체를 print 했을 때 보여줄 문자열을 정의해주는 특수 매서드
#     def __str__(self):
#         return f"{self.name}"
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

p1 = Person("John") # p2와 다른 객체
p2 = Person("John")

print(p1 == p2)

# p = Person("홍길동")
# print(p)
# 결국 __str__의 특수 메서드의 역할은 객체의 멤버변수를 보기위한 방법 p.name 이라는 방법 말고도
# 객체를 호출했을 때 내 멤버변수를 보기위한 용도
