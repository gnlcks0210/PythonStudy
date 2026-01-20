#람다 함수
# - 일반 함수를 더 간결하게 표현하기 위한 방법
# - 변수 이름으로 호출
# - 문법 : 변수명 = lambda 매개변수 : 표현식

#일반 함수 버전
def double_number(x):
    return x*2
print(double_number(3))

# 람다 버전
double_number = lambda x: x * 2
print(double_number(3))

add_number_lambda = lambda num1, num2 : num1 + num2
print(add_number_lambda(3, 5))

# 매개변수 2개를 받고 더 큰수를 구하기
#                                      True일 떄 if 조건식 else False일 때
big_number_lambda = lambda num1,num2 : num1 if num1 > num2 else num2
print(big_number_lambda(10, 7))

#매개변수로 받은 문자열의 길이 출력하기
get_length_lambda = lambda str : print(len(str))
get_length_lambda("hello")

# 1. 매개변수로 숫자 1개를 받고, 짝수면 "짝수입니다" 홀수면 "홀수입니다"
get_number_lambda = lambda num : "짝수입니다." if num % 2 == 0 else "홀수입니다."
print(get_number_lambda(4))

numbers = [1, 2, 3, 4, 5]
double_map = list(map(lambda x : x * 2, numbers))
#print(list(double_map))

# map의 동작 방식
# 1. numbers 리스트를 두번재 인자로 받음
# 2. 빈 리스트 [] 를 하나 만들어둠
# 3. 두번째로 받은 numbers 리스트의 요소를 1개씩 꺼냄
# 4. 꺼낸 요소(1)를 라마 매개변수로 전달
# 5. x=1, x * 2 = 2
# 6. 아까 만들어둔 빈 리스트에 결과 값을 저장 [2]
# 7. 두번재 요소(2)를 람다 매개변수로 전달
# 8. x = 2, x * 2 =4
# 9. 아까 만들어둔 리스트에 결과 값을 저장 [2, 4]

# 리스트로 변환 시키 않은 duble_map 요소 꺼내기
for num in double_map:
    print(num)

numbers = [1, 3, 6, 2, 4, 8, 7, 10, 9]
even_filter = filter(lambda x: x % 2 == 0, numbers)
print(list(even_filter))
# filter의 동작 방식
# 1. numbers 리스트를 두번째 인자로 받음
# 2. 빈 리스트 []를 만들어 둠
# 3. numbers 리스트의 요소를 하나씩 꺼냄
# 4. 꺼낸 요소(1)를 람다 매개변수로 전달
# 5. x = 1, x % 2 == 0의 결과 False이기 때문에 넘어감
# 6. 꺼낸 요소(3)를 람다 매개변수로 전달
# 7. x = 3, x % 2 == 0의 결과 False이기 때문에 넘어감
# 8. 꺼낸 요소(4)를 람다 매개변수로 전달
# 9. x = 4, x % 2 == 0의 결과 True이기 때문에 빈 리스트에 해당 요소 추가 [6]


words = ["Python","JavaScript","HTML","CSS"]
# 문자열의 길이가 5 이상인 요소만 필터링
words_filter = list(filter(lambda str : len(str) >= 5, words))
print(words_filter)
# 요소들을 소문자로 변환 후 저장
words_map = list(map(lambda str : str.lower(), words))
print(words_map)

# 0 보다 큰 수(양수)만 2로 곱한 후 리스트로 저장
nums = [-2, 3, -1, 4]

get_number = list(
    map(lambda x : x * 2,
        filter(lambda x : x > 0, nums)
    )
)

# 구분              map         vs          filter
# 역할           값을 변환                조건이 True인 것만 추가
# 개수             동일                    줄어들 수 있음
# 사용여부      어떻게 값을 바꿀까          특정 값을 거르고 싶다