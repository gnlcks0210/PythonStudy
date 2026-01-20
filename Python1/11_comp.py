# 리스트 컴프리헨션(List Comprehension)
#  - 리스트를 짧고 간결하게 생성할 수 있는 문법

# 리스트 컴프리헨션 버전
nums = [1, 2, 3, 4, 5]
squares = [ n**2 for n in nums ]
print(squares)

# for문 버전
nums = [1, 2, 3, 4, 5]
squares = []

for n in nums:
    squares.append(n**2)


# for문을 사용해서 짝수만 리스트에 추가하기
nums = [1, 2, 3, 4, 5]
evens = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)

# 컴프리헨션 사용해서 짝수만 리스트에 추가하기
nums = [1, 2, 3, 4, 5]

evens = [n for n in nums if n % 2 == 0]
# 1. 가장 먼저 for문 해석
# 2. 첫번째 요소를 꺼냄 (n = 1)
# 3. if문을 해석 (False)
# 4. 조건식의 결과가 거짓이기 때문에 리스트에 요소 추가 X
# 5. 두번째 요소를 꺼냄 (n = 2)
# 6. if문을 해석 (True)
# 7. 조건식의 결과가 참이기 때문에 리스트에 요소(n) 추가

# 입력받은 문자열에서 특정 문자가 몇 번 등장하는지 출력
text = input("문자열 입력: ") # "ABBC"
target = input("찾을 문자 입력: ") # "A"
count = 0

temp_list = sum([count+1 for ch in text if ch == target])
print(temp_list)

# --------------- 딕셔너리 컴프리헨션
words = ["apple", "banana", "cherry"]

result = {word: len(word) for word in words}
print(result)

nums = [1, 2, 3, 4, 5]
# 딕셔너리 저장 형태
#  - 숫자 : "even"
#  - 짝수일때만 요소를 추가

evens = {n: "even" for n in nums if n % 2 == 0}
print(evens)

# 저장 형태는 { 1: "odd", 2: "even" }
#  - 조건 연산자 + 컴프리헨션

evens = {n: "even" if n % 2 == 0 else "odd" for n in nums}

