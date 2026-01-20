#<if문>
# - 특정 조건이 참(True)일 때 실행

num_1 = 10
# num_1이 0 보다 크면 "양수" 출력
if num_1 > 0:
    print("양수")
    print("if문 안에 있습니다.")
print("if문 바깥에 있습니다.")

#사용자로부터 입력을 받고 19세 이상이면 "성인입니다. 출력
# age = int(input("나이를 입력하세요 : ")) #int() 감싸서 형변환
#
# if age >= 19:
#     print("성인입니다.")

# 사용자로 부터 나이와 영화표 유무(y/n)를 입력 받고
# 19세 이상 이면서 영화표가 있으면(y) "입장 가능합니다" 출력

# age = int(input("나이를 입력하세요 : "))
# has_ticket = input("영화표 유무를 써주세요(y/n) : ")
#
# if age >= 19 and has_ticket.upper() == "Y":
#     print("입장 가능합니다.")

#if - elif 문
# age = int(input("나이를 입력하세요 : "))
#
# # 1. 나이가 10세 미만이면 "어린이 입니다."
# # 2. 나이가 20세 미만이면 "10대 입니다."
# # 3. 나이가 30세 미만이면 "20대 입니다."
# # 4. 나이가 40세 미만이면 "30대 입니다."
# if age < 10:
#     print("어린이 입니다.")
# elif age < 20:
#     print("10대 입니다.")
# elif age < 30:
#     print("20대 입니다.")
# elif age < 40:
#     print("30대 입니다.")

#else : 그 외 (위의 조건식이 모두 False)
age = 33

if age < 10:
    print("어린이 입니다.")
elif age < 20:
    print("10대 입니다.")
elif age < 30:
    print("20대 입니다.")
else:
    print("30대 이상입니다.")