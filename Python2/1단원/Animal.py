class Animal:
    def __init__(self, sound):
        self.sound = sound

    # 메소드 ( 함수, 행동)
    def cry(self):
        print(self.sound)

cat = Animal("야옹")
cat.cry()

dog = Animal("멍멍")
dog.cry()