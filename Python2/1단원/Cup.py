class Cup:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand

    def Cafe(self):
        print(f"컵의 색상은 {self.color} \n컵의 브랜드는 {self.brand}")

starCafeCup = Cup("green","starCafe")
starCafeCup.Cafe()
# print("컵의 색상은",starCafeCup.color)
# print("컵의 브랜드는",starCafeCup.brand)

angelCafeCup = Cup("gold","angelCafe")
angelCafeCup.Cafe()
# print("컵의 색상은",angelCafeCup.color)
# print("컵의 브랜드는",angelCafeCup.brand)

blueCafeCup = Cup("blue","blueCafe")
blueCafeCup.Cafe()
# print("컵의 색상은",blueCafeCup.color)
# print("컵의 브랜드는",blueCafeCup.brand)