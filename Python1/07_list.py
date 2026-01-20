# 리스트(list)
#  - 일상 생활에 사용하는 목록과 비슷한 개념
#  - 여러 개의 데이터를 하나의 변수에 저장하고 관리할 수 있음
#    (자료형 상관 없음)

# 특징
#  - 대괄호[] 사용
#  - 값 변경(수정, 삭제, 추가) 가능
#  - 중복 가능

# 요소(Element)
#  - 리스트에 들어가는 각각의 항목을 하나의 요소라고 부름 (값, 데이터)

# 인덱스(index)
#  - 요소의 위치를 의미함
#  - 인덱스를 사용하여 특정 요소에 접근할 수 있음
#  - 항상 0부터 시작(왼쪽 기준)
example = [1, 2.2, True, "Y"]


print(example)
print(example[0])  # 0번 인덱스에 있는 요소에 접근
print(example[2])  # 2번 인덱스에 있는 요소에 접근

example[2] = 100 # 2번 인덱스에 있는 요소의 값을 100으로 변경
print(example[2])

# 음수 인덱스
#  - 오른쪽(끝)에서 시작하는 인덱스(-1부터 시작)
print(example[-1])

example[-3] = 200
print(example[-3])

print(example)

# 이름들이 들어있는 리스트(names)를 만드세요.
# 요소 : “kim”, “lee”, “park”, “choi”, “min”, “jung”, “jeon”
names = ["kim", "lee", "park", "choi", "min", "jung", "jeon"]
# 양수 인덱스를 활용하여 park을 출력하세요.
print(names[2])
# 양수 인덱스를 활용하여 min을 출력하세요.
print(names[4])
# 음수 인덱스를 활용하여 choi를 출력하세요.
print(names[-4])
# 음수 인덱스를 활용하여 lee를 출력하세요.
print(names[-6])

# 슬라이싱
#  - 인덱스를 활용하여 특정 요소를 추출하거나 일부를 잘라내는 기능을 수행

# 슬라이싱 문법 : 리스트[start:stop:step]
#  - start : 시작 인덱스
#  - stop : 끝 인덱스
#  - step : 건너 뛰기
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[1:6]) # 1번 인덱스부터 5번 인덱스까지
print(numbers[2:]) # 2번 인덱스부터 끝까지
print(numbers[:2]) # 맨 처음(0번 인덱스)부터 1번 인덱스 까지 (2-1)
print(numbers[3:8:3]) # 3번 인덱스부터 7번 인덱스(8-1)까지, 3칸씩 건너뜀

# 20부터 70까지의 범위를 추출 하는데
# step을 줘서 [20, 50] 만 가져오게
print(numbers[1:7:3])

# -----------------------------------------------------------
# append()
#  - 리스트의 끝에 요소 추가
a_list = [1, 2, 3]
a_list.append(4) # a_list의 끝에 4를 추가하겠다.
print(a_list) # [1, 2, 3, 4]

# extend()
#  - 리스트를 연결시켜주는 기능을 수행
e_list = [1, 2, 3]

e_list.append([4, 5, 6]) # 리스트인채로 요소에 추가
print(e_list)
print(e_list[3])

e_list.extend([7, 8, 9]) # 기존 리스트와 추가한 리스트를 연결
print(e_list)

# insert()
#  - 특정 인덱스에 요소 추가
#  - insert(인덱스, 값)
i_list = [1, 2, 3]
i_list.insert(1, 100)
print(i_list)

# pop()
#  - 특정 인덱스의 요소를 삭제
p_list = [1, 2, 3]
p_list.pop(2)
print(p_list)

# remove()
#  - 특정 값을 가진 요소를 삭제
r_list = [1, 2, 3]
r_list.remove(1)
print(r_list)

# clear()
#  - 리스트의 요소 전체 삭제
c_list = [1, 2, 3]
c_list.clear()
print(c_list)

# -----------------------------------------------
# 리스트를 사용할 때 알면 유용한 것들

# 1. len()
#  - 파이썬에서 제공하는 내장 함수
#  - 리스트의 길이를 반환
computer_science = ["파이썬", "자바", "알고리즘"]
print(len(computer_science)) # 리스트의 길이를 출력 : 3

# - len(computer_science)의 결과는 3
# - range(3)  -> 0부터 2까지 반복
for i in range(len(computer_science)):
    # 처음 반복문 돌때 i = 0이므로 computer_science[0]
    # 두번째 반복문 돌때 i = 1이므로 computer_science[1]
    # 세번째 반복문 돌때 i = 2이므로 computer_science[2]
    print(computer_science[i])

# 2. sort()
#  - 리스트를 정렬시켜주는 메서드
#  - 원본이 변경됨
#  - 기본적으로 오름차순 정렬
sort_numbers = [2, 3, 7, 5, 1, 9]
sort_numbers.sort()
print(sort_numbers)

# 내림차순 정렬은 sort(reverse=True)
sort_numbers.sort(reverse=True)
print(sort_numbers)

# 3. sorted()
#  - 리스트를 정렬시켜주는 내장 함수
#  - 원본 리스트에 영향을 주지 않음
#  - 기본적으로 오름차순으로 동작
number_list = [1, 6, 4, 2, 8, 9, 5]

# a. 비어있는 리스트를 생성해둠
#    -> 새로운 리스트 : []
# b. 원본 리스트에 있는 요소를 하나씩 꺼내서 옮김
#    -> 새로운 리스트 : [1, 6, 4, 2, 8, 9, 5]
# c. 새로운 리스트를 정렬시킴
#    -> 새로운 리스트 : [1, 2, 4, 5, 6, 8, 9]
# d. 정렬이 완료된 새로운 리스트를 되돌려줌
sorted_number_list = sorted(number_list)
print(f"sorted() 오름차순 정렬 : {sorted_number_list}")

# 내림차순은 똑같이 reverse=True
reverse_number_list = sorted(number_list, reverse=True)
print(f"sorted() 내림차순 정렬 : {reverse_number_list}")

# 4. reverse()
#  - 리스트의 순서를 뒤집음 (메서드)
#  - 원본 리스트가 영향을 받음
reverse_numbers = [1, 2, 3, 4, 5]
reverse_numbers.reverse()
print(f"reverse() : {reverse_numbers}")

# 5. in 키워드
#  - 리스트에 특정 값이 있는지 확인
#  - 있다면 True, 없다면 False
in_numbers = [1, 2, 3, 4, 5]
if 4 in in_numbers:
    print("리스트에 숫자 4가 존재합니다.")

# -----------------------------------------------------
numbers = [[1,2,3],[4,5,6],[7,8,9]]

# 숫자 4 출력
print(numbers[1][0])

# 숫자 8출력
print(numbers[2][1])


