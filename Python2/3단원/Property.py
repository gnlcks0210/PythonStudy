# property를 사용해보는 것
# getter, setter를 사용해서 비공개 변수를 가져오고 수정해보기
#Person으로 class를 선언할꺼다.
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    # 이 아래가 중요
    # 1. property에서 getter를 선언하는 방법
    # getter : 접근할 수 없는 변수를 가져오게 해주는 것
    @property
    def age(self):
        return self.__age

    # 2. setter를 선언하는 방법
    # setter : 접근할 수 없는 변수를 수정하게 해주는 것
    @age.setter
    def age(self,value):
        self.__age = value

#**********************************************************************
# 아래가 실행부분 위에는 설계부분
p = Person("철수",30)
print(p.age)
p.age = 20
print(p.age)