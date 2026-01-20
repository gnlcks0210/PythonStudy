class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def add_score(self,point):
        self.score+=point

    def show_info(self):
        print(f"{self.name} {self.score}점")

student1 = Student("김철수",80)
student2 = Student("이영희",70)
student1.show_info()
student1.add_score(10)
student1.show_info()
student2.show_info()

