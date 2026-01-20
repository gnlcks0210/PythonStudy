class Animal():
    def speak(self):
        print("동물 소리를 냅니다.")

class Dog(Animal):
    def speak(self):#메서드 오버라이딩(함수 오버라이드)
        print("멍멍")

dog = Dog()
dog.speak()