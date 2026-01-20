# Q1. sum_to_n()
# - 사용자로부터 숫자 1개(n)를 입력받습니다.
# - 1부터 사용자가 입력한 숫자 n까지의 합을 출력
# ex) 사용자가 10 입력하면 1+2+3+4+5+6+7+8+9+10

def sum_to_n():
    n = int(input("숫자1개를 입력해 주세요 : "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)
sum_to_n()

# Q2. print_diff()
# - 매개변수로 숫자 2개를 전달받아 두 수의 차이를 출력하세요.
# - 조건 : 큰 수 - 작은수로 계산되어야 한다.
# - 첫번째 매개변수에 큰 수가 올수도, 두번재 매개변수에 큰 수가 올수도 있습니다.
def print_diff(num1, num2):
    if num1 > num2:
        print(num1 - num2)
    else:
        print(num2 - num1)
print_diff(1, 2)

# Q3. avg_of_three()
# - 매개변수 3개를 전달 받습니다.
# - 평균을 구한 후 반환하세요.
# - 반환 받은 값을 avg 변수에 저장 후 출력하세요.

def avg_of_three(num1,num2,num3):
    return (num1 + num2 + num3) // 3

avg = avg_of_three(1, 2, 3)
print(avg)

# Q4. is_even()
# - 리스트를 매개변수로 받아서 짝수의 개수만 반환
numbers = [1,2,3,4,5,6,7,11,15]
def is_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count
event_count = is_even(numbers)
print(event_count)




# ----- 학생 성적 프로그램 -----
SUBJECTS = ("국어", "영어", "수학", "과학")

# 1. 학생을 추가하는 함수 add_student() 작성
#  - "[이름] 학생이 추가되었습니다." 반환
#  - (선택) 이미 존재하는 이름일 경우 "이미 존재하는 학생입니다." 반환
def add_student(students, name):
    if name in students:
        return "이미 존재하는 학생입니다."
    students[name] = {s : 0 for s in SUBJECTS}
    # 저장 예시
    # students = {
    #   "홍길동" = {"국어" : 0, "영어" : 0, "수학" : 0, "과학" : 0}
    # }
    return f"{name} 학생이 추가되었습니다."

# 2. 학생을 삭제하는 함수 remove_student() 작성
#  - "[이름] 학생이 삭제되었습니다." 반환
#  - (선택) 존재하는 이름이 없을 경우 "해당 학생이 없습니다." 반환
def remove_students(students, name):
    if name not in students:
        return "해당 학생이 없습니다."
    students.pop(name)
    return f"{name} 학생이 삭제되었습니다."

# 3. 점수를 저장하는 함수 set_score() 작성
#  - "[이름] 학생의 [과목] 점수가 [점수]로 저장되었습니다." 반환
#  - (선택) 존재하는 이름이 없을 경우 "해당 학생이 없습니다." 출력
#  - (선택) 존재하는 과목이 없을 경우 "존재하지 않는 과목입니다." 출력
#  - (선택) 점수가 0 미만 또는 100 초과일 경우 "점수는 0~100점 사이여야 합니다." 출력
def set_score(students, name, subject, score):
    if name not in students:
        return "해당 학생이 없습니다."

    if subject not in students[name]:
        return "존재하지 않는 과목입니다."

    if score < 0 or score > 100:
    #if not(0<= score <=100):
        return "점수는 0~100점 사이여야 합니다."

    students[name][subject] = score

    return f"{name} 학생의 {subject} 점수가 {score}로 저장되었습니다."

# 4. 특정 학생의 합계 점수를 반환하는 함수 student_total() 작성
#  - 학생의 합계 점수를 반환
#  - (선택) 존재하는 이름이 없을 경우 "None" 반환
def student_total(students,name):
    if name not in students:
        return None
    return sum(students[name].values())
# 5. 특정 학생의 평균 점수를 반환하는 함수 student_avg() 작성
#  - 학생의 평균 점수 반환
#  - (선택) 존재하는 이름이 없을 경우 "None" 반환
def student_avg(students,name):
    total_score = student_total(students,name)

    # student에서 name 이라는 키가 존재하지 않을 경우 None 반환
    # 위의 조건이 False 이면 total_score / len(SUBJECTS) 가 연산된 결과 반환
    return None if name not in students else total_score / len(SUBJECTS)

# 6. 학생 정보를 출력하는 함수 print_student() 작성
#  - "총점: [합계], 평균: [평균]" 출력
#  - (선택) 존재하는 이름이 없을 경우 "해당 학생이 없습니다." 출력
def print_student(students, name):
    if name not in students:
        print("해당 학생이 없습니다.")
        return

    for subject,score in students[name].items():
        print(f"과목 : {subject}, 점수 : {score}")

    total_score = student_total(students, name)
    avg_score = student_avg(students, name)
    print(f"총점 : {total_score}, 평균 : {avg_score}")

# 7. 학생들의 전체 리스트를 조회하는 함수 print_all() 작성
#  - 전체 학생의 이름을 출력
#  - (선택) 학생 목록이 없을 경우 "학생 목록이 비어 있습니다." 출력
def print_all(students):
    if students is None:
        print("학생 목록이 비어 있습니다.")
    for name in students.keys():
        print(f"학생의 이름 : {name}")
def run_students():
    students = {}
    while True:
        print("\n=== 학생 성적 프로그램 ===")
        print("1. 학생 추가")
        print("2. 학생 삭제")
        print("3. 점수 입력/수정")
        print("4. 학생 성적 조회")
        print("5. 전체 학생 목록")
        print("0. 종료")
        choice = input("번호: ").strip()

        if choice == "1":
            # 학생의 이름을 입력받고 add_student() 함수를 호출 및 반환된 문자열을 출력하세요.
            name = input("추가할 학생의 이름 : ")
            msg = add_student(students, name)
            print(msg)
        elif choice == "2":
            # 삭제할 학생의 이름을 입력받고 remove_student() 함수를 호출 및 반환된 문자열을 출력하세요.
            name = input("삭제할 학생의 이름 : ")
            msg = remove_students(students, name)
            print(msg)
        elif choice == "3":
            # 학생의 이름, 과목(국어/영어/수학/과학), 점수를 입력받고 set_score() 함수를 호출 및 반환된 문자열을 출력하세요.
            name = input("학생 이름 : ")
            subject = input("과목 : ")
            score = int(input("점수 : "))
            msg = set_score(students,name, subject, score)
            print(msg)
        elif choice == "4":
            # 조회할 학생의 이름을 입력받고 print_student() 함수를 호출하세요.
            name = input("학생 이름 : ")
            print_student(students, name)
        elif choice == "5":
            # print_all() 함수를 호출하세요.
            print_all(students)
        elif choice == "0":
            # "프로그램을 종료합니다"를 출력하고 반복문을 종료하세요.
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

run_students()
