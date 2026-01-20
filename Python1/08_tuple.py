# 튜플
#  - 리스트와 거의 유사한 형태를 가짐

# 특징
#  - 소괄호() 사용
#  - 값 변경(수정, 삭제, 추가) 불가능, 조회만 가능
#  - 중복 허용
names = ("kim", "lee", "park")

print(names[1])
# names[0] = "jung"    수정 불가!
print(names[0])

tuple_alphabet = ("a", "a", "b", "c")
print(tuple_alphabet.count("a"))  # 특정 값을 가진 요소의 개수
print(tuple_alphabet.index("a"))  # 특정 값을 가진 요소의 인덱스
