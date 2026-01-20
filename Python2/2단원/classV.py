class Student:
    # 클래스 변수
    subject = "Art" # 클래스 내부에서 사용하는 변수

    def __init__(self,name, ban):
        self.name = name
        self.ban = ban

    def introduce(self):
        print(f"안녕하세요, 제 이름은 {self.name} 입니다.")
        print(f"저는 {self.ban}반 입니다.")
        if(self.subject == "Art"):
            print(f"1교시 수업은 {self.subject} 입니다.")
        elif(self.subject == "English"):
            print(f"3교시 수업은 {self.subject} 입니다.")
        else:
            print(f"2교수 수업은 {self.subject} 입니다.")

tom = Student("tom","A")
jason = Student("jason","A")
tom.introduce()
jason.introduce()
print("-----------------------------------------")
Student.subject = "English"
tom.introduce()
jason.introduce()


