# 세트
# - 순서가 없고 중복된 값을 허욯하지 않는 자료구조

#특징
# -중괄호 {} 사용
# - 중복 불가
# - 순서를 보장하지 않음

numbers = {1,2,3,2}
# print(numbers[0]) # 요소에 직접 접근이 불가능

str_random = "aaaabbbbbbwwwwwwwwdddderwerwerwerwer"
str_random = set(str_random) # set 으로 변환 (중복 제거)
print(str_random) # 전체 출력(순서를 보장하지 않음)

list_str = list(str_random) # 리스트로 변환
list_str.sort()# 변환된 리스트를 정렬
print(list_str)

