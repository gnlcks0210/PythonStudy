# Q1. 문자열 앞에 Hello 붙이기
front_Hello = lambda x : "Hello" + x
print(front_Hello("World"))

comp_q1 = ["Hello" + str for str in ["python", "java", "php"]]
print(comp_q1)

# Q2. 숫자를 1개 받아서 10 이상이면 " 10 이상입니다."
#       10미만이면 "10미만입니다."
num = int(input("숫자를 입력하세요 : "))

over_ten = lambda n : "10 이상입니다." if n >= 10 else "10미만입니다."
print(over_ten(num))

comp_q2 = ["10이상입니다." if n >= 10 else "10미만입니다." for n in [num]]
print(comp_q2)

# Q3. 아래의 리스트에서 20이상인 숫자만 리스트 형태로 저장
# numbers = [10, 20, 33, 17]

numbers = [10, 20, 33, 17]
get_numbers = list(filter(lambda x : x >= 20, numbers))
print(get_numbers)

comp_q3 = [n for n in numbers if n >=20 ]
print(comp_q3)

# Q4. 아래의 리스트에서 60점 이상은 True, 미만은 False 출력
# scores = [55, 66,73]

scores = [55, 66,73]
get_scores = list(map(lambda x : x >= 60, scores))
print(get_scores)

comp_q4 = [ s >= 60 for s in scores]
print(comp_q4)


# Q5. 아래의 리스트에서 5글자 이상인 단어만 소문자로 변환
# words = ["Python", "Java", "PHP"]

words = ["Python", "Java", "PHP"]
get_words = list(map(lambda word : word.lower(),filter(lambda word : len(word) >= 5, words)))
print(get_words)

comp_q5 = [w.lower() for w in words if len(w) >= 5]
print(comp_q5)

# Q6. 아래의 리스트에서 50점 이상인 점수만 출력
# scores = [44,52,78]
# 출력 예시 : ["52점 합격" , "78점 합격"]

scores = [44,52,78]
over_scores = list(
    map(lambda score : f"{score}점 합격",
        filter(lambda score : score >= 50,scores)
    )
)
print(over_scores)

comp_q6 = [f"{s}점 합격" for s in scores if s >= 50]
print(comp_q6)


# Q7. 아래의 리스트에서 숫자만 필터 후 int() 타입으로 변환
# data = ["1", "a", "b", "3", "7"]
# 숫자 판별 방법 : 문자열.isdigit()

data = ["1", "a", "b", "3", "7"]

is_number = list(
    map(lambda x : int(x) ,
        filter(lambda x : x.isdigit(),data))
)
print(is_number)

comp_q7 = [int(x) for x in data if x.isdigit()]
print(comp_q7)