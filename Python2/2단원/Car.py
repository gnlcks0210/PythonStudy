class Car:
    def __init__(self,color):
        self.color = color

    def ride(self):
        print(self.color, "car is riding")

class Bus(Car):
    def __init__(self, color, bell_sound):
        super().__init__(color)
        self.bell_sound = bell_sound

    def press_bell(self):
        print(self.bell_sound)

bus = Bus(color = "red", bell_sound="Ding-Dong")
bus.ride()
bus.press_bell()
