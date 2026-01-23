from cafe import Cafe

# 1. 객체를 선언
c = Cafe()

# 2. show_menu 함수를 호출
c.show_menu()

# 3. 주문 받기
menu = input("\n주문할 메뉴를 입력하세요\n")

# 4. result에다가 order 함수의 반환 값을 저장
result = c.order(menu)

# 5. 출력
print(result)