class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod # 클래스 함수
    def from_string(cls, s):
        name, age_str = s.split("-")
        age = int(age_str)
        return cls(name, age)

p = Person.from_string("Kim-30")
print(type(p),p.name,p.age)