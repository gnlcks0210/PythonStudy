#함수 (Function)
# - 특정 기능을 수행하는 여러 줄의 코드를 하나의 블록으로 묶어 놓은 것

#매개 변수
# - 함수를 호출할 때 전달되는 값

# def 함수명(매개변수1, 매개변수2):
def hello(name):
    print("안녕하세요.")
    print(f"제 이름은 {name}입니다.")
    print("만나서 반갑습니다.")

#      인자
hello("엄휘찬") # 함수 호츨
hello("홍길동")
hello("철수")

def add(num1, num2):
    print(num1 + num2)

add(20, 30)
add(306, 204)
add(5, 7)

# 함수 이름: introduce
# 이름과 나이를 매개변수로 받음
# 출력 형식: "이름은 OOO이고 나이는 OO살 입니다."

def introduce(name, age):
    print(f"이름은 {name}이고 나이는 {age}살 입니다.")

introduce("엄휘찬", 24)


#return
# - 값을 함수가 호출된 곳을 반환 시켜주는 키워드
def sub(num1, num2):
    return num1 - num2

print(sub(50,30))

result = sub(50,15)
print(result)

#add_two_numbers() 함수
# - 사용자로부터 2개의 숫자를 입력받음
# - 덧셈 결과를 출력

def add_two_numbers():
    num1 = int(input("숫자1을 입력하세요. : "))
    num2 = int(input("숫자2을 입력하세요. : "))

    print(num1 + num2)

add_two_numbers()

# 카페 주문 프로그램

# 1. 메뉴판을 조회하는 함수
def print_menu(menu):
    print("-----메뉴판-----")

    for no, (name, price) in menu.items():
        print(f"{no}. {name} - {price}원")
# 2. 장바구니를 출력하는 함수
# - 출력 형식 : "0. 아메리카노 X 5 = 10000원"
def print_cart(cart):
    for index,dict in enumerate(cart):
        print(f"{index}. {dict['name']} X {dict['count']} = {dict['price'] * dict['count']}")

# 3. 장바구니에 메뉴를 추가하는 함수
def add_to_cart(menu, cart, no, count):
    # menu에 있는 음료 이름과 가격을 불러와야 함
    # 예시 : 사용자가 1번 메뉴를 선택(no = 1)
    #       menu[no] -> 1이라는 키를 가진 값을 가져옴 -> ("아메리카노", 2000)

    name,price = menu[no]

    # cart 리스트에 추가해야 함
    # - [{"name":"아메리카노", "price":2000, "count":3}]
    cart.append(({"name": name, "price": price, "count": count}))

    # #아메리카노 3개가 추가되었습니다" 반환
    return f"{name} {count}개가 추가되었습니다."

# 4. 장바구니 특정 항목을 제거하는 함수
def remove_from_cart(cart, index):
    remove_item = cart.pop(index)
    return f"{remove_item['name']}이(가) 삭제되었습니다."

# 5. 장바구니 특정 항목의 수량을 변경하는 함수
def update_count(cart, index , new_count):
    cart[index]["count"] = new_count
    return f"{cart[index]['name']}의 수량이 {new_count}개로 변경되었습니다."

# 6. 장바구니의 합계 금액을 구하는 함수
# - "장바구니의 총 금액은 OOO원 입니다." 반환
def cart_sum(cart):
    total = 0
    for dict in cart:
            total += dict['price'] * dict['count']
    return f"장바구니의 총 금액은 {total}원 입니다."

menu = {
    1: ("아메리카노",2000),
    2: ("카페라떼", 3000),
    3: ("자몽에이드", 3500),
    4: ("카푸치노", 3200)
}

cart = []

while True:
    print("-----카페 주문 프로그램-----")
    print("1. 메뉴보기")
    print("2. 장바구니 보기")
    print("3. 장바구니 추가")
    print("4. 장바구니 삭제")
    print("5. 장바구니 수량 수정")
    print("6. 합계 금액 조회")
    print("0. 프로그램 종료")

    choice = input("번호 : ")

    if choice == "1":
        print_menu(menu)
        # 아무 동작 안함
        # 문법적을 코드가 반드시 있어야하는 자리에 사용
        # - "나중에 작성하겠다." 라는 의미를 가짐
        # pass
    elif choice == "2":
        print_cart(cart)

    elif choice == "3":
        no = int(input("장바구니에 담을 메뉴 번호를 입력하세요 : "))
        count = int(input("수량 : "))

        msg = add_to_cart(menu, cart, no, count)
        print(msg)
        print(cart)
    elif choice == "4":
        index = int(input("장바구니에서 삭제할 인덱스 : "))
        msg = remove_from_cart(cart, index)
        print(msg)

    elif choice == "5":
        index = int(input("장바구니에서 수정할 인덱스 : "))
        new_count = int(input("새 수량 : "))
        msg = update_count(cart, index, new_count)
        print(msg)

    elif choice == "6":
        msg = cart_sum(cart)
        print(msg)
    elif choice == "0":
        break
    else:
        pass




#-------------------------------
# 스코프(Scope)
# - 변수가 유효한 범위

#LEGB
# - Local : 함수 내부에서 정의된 변수 (지역 변수)
# - Enclosing : 중첩 함수에서 바깥쪽 함수의 변수
# - Global : 파일 전체에서 접근 가능한 변수 (함수 밖에서 선언됨, 전역 변수)
# - Built-in : 파이썬에서 제공하는 내장 함수를 위한 공간(len, print, range 등)

#함수 스코프의 동작 순서
# - Local -> Enclosing -> Global -> Built-in 순서

# Global scope
# -전역 변수
# - 함수 바깥에서 선언된 변수
# - 모든 위치(함수 포함)에서 사용이 가능한 변수
y = 10 #  Global Scope 전역 변수

# Local Scope
# -지역 변수
# - 함수 내부에서 선언된 변수
# - 함수 내부에서만 사용이 가능한 변수
def get_x():
    x = 30 # local Scope 지역 변수
    print(x)

get_x()

# 전역 함수
# - 프로그램 전체에서 사용 가능한 함수 (어디서든 호출이 가능)
# - 여태 수업중에 작성한 함수들이 모두 전역 함수

# 지역 함수
# - 특정 함수 내부에서 정의된 함수
# - 특정 함수 내부에서만 호출 가능

x = 10 # Global (전역 변수)
def outer(): #Global (전역 함수)
    print("지역 함수 호출 전")

    y = 20 # Enclosing
    def inner(): # Local (지역 함수)
        z = 30 #Local (지역 변수)
        print("지역 함수 inner()가 호출되었습니다.")
    inner()
    print("지역 함수 호출 완료")

outer()

count  = 10

def add_test():
    global count #이 변수는 전역 변수다
    # 함수 내부에서는 대입 연산(=)을 사용하게 되면 지역 변수로 인식
    count = count + 10

    print(count)