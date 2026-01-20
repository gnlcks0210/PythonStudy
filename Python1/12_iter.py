# 이터레이터(Iterator)
#  - 한번에 하나씩 값을 꺼낼 수 있는 객체
#  - next()라는 내장 함수를 통해 다음 값을 가져옴

# 이터러블(Iterable)
#  - 반복 가능한 객체
#  - 리스트, 튜플, 문자열 등을 이터러블한 객체라고 표헌
#  - for문으로 꺼낼 수 있는 객체를 의미함

# 리스트
#  - 이터러블 O
#  - 이터레이터 X
nums = [1, 2, 3, 4, 5]
it = iter(nums) # 리스트를 이터레이터로 변환

print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # 4
print(next(it)) # 5
# print(next(it)) # StopIteration : 더이상 꺼낼 값이 없어서 발생

nums = [10, 20, 30, 40]
it = iter(nums) # 이터레이터 객체로 변환

print(next(it)) # 10
print(next(it)) # 20

for n in it:
    print(n)


text = "ABC" # 이터러블
it = iter(text) # 이터레이터 객체로 변환

print(next(it)) # A










