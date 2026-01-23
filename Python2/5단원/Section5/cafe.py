class Cafe:
    def __init__(self):
        self.Americano_price = 4500
        self.latte_price = 5000
        self.cappuccino_price = 5000
        self.menu = {"아메리카노" : self.Americano_price,
                     "라떼" : self.latte_price,
                     "카푸치노" : self.cappuccino_price}

    def show_menu(self):
        print("메뉴판")
        for key, value in self.menu.items():
            print(f"- {key} : {value}")

    def order(self, order):
        if order in self.menu.keys():
            return f"{order} 주문 완료! 가격은 {self.menu[order]}원 입니다."
        else:
            return "해당 메뉴가 없습니다."
