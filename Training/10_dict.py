# Q1. 빈 딕셔너리 생성(person) 후 아래의 정보를 추가하세요
# - name : Alice
# - age : 25
# -city : Seoul
# - 다 만들면 "age" 값을 1 증가시키고 전체 딕셔너리를 출력하세요.

person = {}
person["name"]  = "Alice"
person["age"] = 25
person["city"] = "Seoul"
person["age"] += 1
print(person)


#Q2. 과목 점수가 담긴 딕셔너리를 생성하세요.
# - scores = {"kor" : 85, "eng" : 90, "math": 70}
# - 평균 점수 계산 후 출력
# - 80점 미만 과목의 이름과 점수 출력
print("")
scores = {"kor" : 85, "eng" : 90, "math" : 70}
total = 0
for key,value in scores.items():
    total += value
    if value < 80:
        print(f"{key} : {value}")
print(f"평균 : {total//len(scores.keys())}")
#2번 문제 빠르게 풀면
# - 사용자로부터 국어, 영어, 수학 성적을 직접 입력받아 딕셔너리에 추가
# - 가장 높은 점수를 받은 과목과 가장 낮은 점수를 받은 과목 출력

print("")
# for key in scores.keys():
#     scores[key] = int(input("점수를 입력하세요 : "))
#
# values = scores.values()
# sort_values = sorted(values,reverse = True)
# print(f"가장 높은 점수 : {sort_values[0]}")
# print(f"가장 낮은 점수 : {sort_values[len(sort_values)-1]}")

# Q1. 빈 딕셔너리 profile을 만들고 아래 정보를 추가하세요.
#  - nickname : neo
#  - level : 3
#  - region : Incheon
#  - 이후 레벨을 2 증가시키고, region을 Seoul로 변경한 뒤 출력하세요.
print("")

profile = {}
profile["nickname"] = "neo"
profile["level"] = 3
profile["region"] = "Incheon"

profile["level"] += 2
profile["region"] = "Seoul"

print(profile)


# Q2. 재고를 관리하는 딕셔너리에서 재고가 3개 미만인 품목의 이름과 재고를 출력하세요.
#  - stock = {"pen": 5, "note": 2, "eraser": 0, "ruler": 3}
#  - 출력 형식 : [품목]의 재고는 [재고]개가 남았습니다.
print("")
stock = {"pen": 5, "note": 2, "eraser": 0, "ruler": 3}

for key,value in stock.items():
    if value < 3:
        print(f"{key} : {value}")

# Q3. 제품을 관리하는 딕셔너리에서 아래의 조건에 맞게 출력하세요.
#  - products = {"notebook": 1200000, "tablet": 600000, "mouse": 25000, "monitor": 300000}
#  - 가장 비싼 상품을 출력하세요.
#    > "가장 비싼 상품은 [상품명]이고 가격은 [가격]원 입니다."
#  - 가장 저렴한 상품을 출력하세요.
#    > "가장 저렴한 상품은 [상품명]이고 가격은 [가격]원 입니다."
print("")
products = {"notebook": 1200000, "tablet": 600000, "mouse": 25000, "monitor": 300000}

values = products.values()
sort_values = sorted(values)

for key, value in products.items():
    if sort_values[0] == value:
        print(f"가장 비싼 상품은 {key}이고 가격은 {value}원 입니다.")
    if sort_values[len(sort_values)-1] == value:
        print(f"가장 저렴한 상품은 {key}이고 가격은 {value}원 입니다.")

# Q4. 학생들의 출석을 관리하는 딕셔너리에서 아래의 조건에 맞게 출력하세요.
#  - attendance = {"kim": 18, "lee": 22, "park": 15, "choi": 20}
#  - 전체 학생들의 평균 출석 횟수를 출력하세요.
#  - 출석 횟수가 20회 이하인 학생의 이름과 횟수를 아래의 출력에 맞게 출력하세요.
#    > "출석이 20회 이하인 학생들의 목록입니다."
#    > "[이름1]의 학생 출석 횟수는 [횟수1]번 입니다."
#    > "[이름2]의 학생 출석 횟수는 [횟수2]번 입니다."
#    > "[이름3]의 학생 출석 횟수는 [횟수3]번 입니다."
print("")
attendance = {"kim": 18, "lee": 22, "park": 15, "choi": 20}

total = 0
print("출석 횟수가 20회 이하인 학생들의 목록입니다.")
for key,value in attendance.items():
    total += value
    if value <= 20:
        print(f"[{key}]의 학생 출석 횟수는 [{value}]입니다.")
print(f"전체 학생들의 평균 출석 횟수{total/len(attendance.keys())}")

# Q5. 장바구니 딕셔너리에서 아래의 조건에 맞게 출력하세요.
#  - cart = {"mouse": 12000, "keyboard": 35000, "usb": 8000, "monitor": 150000}
#  - 모든 품목의 총 금액을 계산하여 출력하세요.
#  - 가격이 20,000원 이상인 품목만 "[품목]의 가격은 [가격]원 입니다."를 출력하세요.
#  - 총 금액이 100,000원 이상이면 총 금액에 10% 할인을 적용한 최종 결제 금액을 출력하세요.
#    > 10% 할인된 최종 결제 금액은 "총 금액 / 0.9"로 계산하면 됩니다.
#    > "최종 결제 금액은 [금액]원 입니다." 출력
print("")
cart = {"mouse": 12000, "keyboard": 35000, "usb": 8000, "monitor": 150000}
total = 0
for key,value in cart.items():
    total += value
    if value >= 20000:
        print(f"[{key}]의 가격은 [{value}]원 입니다.")

print(total)
if total >= 100000:
    print(f"최종 결제 금액은 [{total*0.9}]원 입니다.")
# --------------------------------------------------------------------
# <List + Set 활용>
# Q1. 리스트에 저장된 값 중에서 사용자가 입력한 숫자가 몇 번 나오는지, 가장 많이 등장한 숫자는 무엇인지 출력하세요.
#  - numbers = [1, 3, 5, 3, 2, 3, 4, 3, 2]
#  - target = int(input("찾고 싶은 숫자를 입력하세요: "))
#  - 출력 : "2은 2번 등장합니다."
#  - 출력 : "가장 많이 등장한 숫자는 3입니다."
#  - 이후 리스트 안의 중복된 숫자를 제거하고, 제거된 리스트를 오름차순으로 정렬 후 출력하세요.
#  - 출력 : "중복 제거 및 오름차순 정렬 후 리스트 : "

# 오름차순 정렬은 sort, sorted를 한번 사용해서 풀어보고
# 다 풀었다면 sort, sorted를 사용하지 않고 정렬 알고리즘에 대해 찾아보고 직접 풀어보시면 더욱 좋습니다.

numbers = [1, 3, 5, 3, 2, 3, 4, 3, 2]
target = int(input("찾고 싶은 숫자를 입력하세요: "))
largest_number = 0
count = 0
number = 0
for num in numbers:
    if target == num:
        count += 1
print(f"{target}은 {count}번 등장합니다.")
for num in numbers:
    count = 0
    for n in numbers:
        if num == n:
            count += 1
    if count > largest_number:
        largest_number = count
        number = num
print(f"가장 많이 등장한 숫자는 {number}입니다.")

set_numbers = set(numbers)

#sort,sorted 사요 하고 풀 경우
# list_numbers = list(set_numbers)
# print(sorted(list_numbers))

#사용하지 않을 경우