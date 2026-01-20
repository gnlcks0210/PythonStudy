# 문자열의 길이가 5 이상인 단어만 추출하기
animals = ["cat", "dog", "elephant", "tiger"]
result = []

for animal in animals:
    if len(animal) >= 5:
        result.append(animal)

# 위의 코드를 리스트 컴프리헨션으로 변경해보세요.
result = [animal for animal in animals if len(animal) >= 5]