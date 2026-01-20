# 사용자로부터 점수(score)를 입력 받습니다.

# 90점 이상은 "A학점 입니다.!"
# 80점 이상은 "B학점 입니다.!"
# 70점 이상은 "C학점 입니다.!"
# 60점 이상은 "D학점 입니다.!"
# 60점 미만은 "F학점 입니다.!"

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("A학점 입니다.!")
elif score >= 80:
    print("B학점 입니다.!")
elif score >= 70:
    print("C학점 입니다.!")
elif score >= 60:
    print("D학점 입니다.!")
else:
    print("F학점 입니다.!")

#------------------------------------
# 사용자로부터 월(month)를 입력 받습니다.
# 3월, 4월, 5월은 "봄" 출력
# 6월, 7월, 8월은 "여름" 출력
# 9월, 10월, 11월은 "가을" 출력
# 12월, 1월, 2월은 "겨울" 출력
# 그 외의 숫자는 "잘못된 월을 입력하셨습니다." 출력

month = int(input("월(month)를 입력해주세요 : "))

#범위로 풀기

if month >=3 and month <= 5:
    print("봄")
elif month >=6 and month <= 8:
    print("여름")
elif month >= 9 and month <=11:
    print("가을")
elif month == 12 or 0< month <=2:
    print("겨울")
else:
    print("잘못된 월을 입력하셨습니다.")

#or 연산자로 풀기
# if month == 3 or month == 4 or month == 5:
#     print("봄")
# elif month == 6 or month == 7 or month == 8:
#     print("여름")
# elif month == 9 or month == 10 or month == 11:
#     print("가을")
# elif month == 1 or month == 2 or month == 12:
#     print("겨울")
# else:
#     print("잘못된 월을 입력하셨습니다.")