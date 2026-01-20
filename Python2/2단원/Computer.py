class Computer:
    def powerOn(self):
        print("Power on")
    def powerOff(self):
        print("Power off")

class Samsung(Computer):
    def powerOn(self):  # 메소드 오버라이딩
        print("마이 러브 삼성")

# 1. 상속을 받아야한다 : 자식에서 재정의를 해야하기 때문
# 2. 부모의 메서드 이름과 동일 : 함수 오버라이드가 됩니다.

samsung = Samsung()
samsung.powerOn()
samsung.powerOff()