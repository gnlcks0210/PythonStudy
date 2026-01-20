class Employee:
    def __init__(self,name,position):
        print("Employee 생성자입니다")
        self.name=name
        self.position=position

    def introduce(self):
        print(f"안녕하세요. 저는 {self.position} {self.name}입니다.")

class Developer(Employee):
    def __init__(self,name,position,language):
        print("Developer 생성자입니다.")
        super().__init__(name,position)
        print("super() 실행 완료")
        self.language=language

    def coding(self):
        print(f"{self.name} 이(가) {self.language} 언어로 코딩 중입니다.")

dev = Developer("엄휘찬","개발자","Python")
dev.introduce()
dev.coding()
