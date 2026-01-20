# 딕셔너리(Dictionary)
# - 키(key)와 값(value)이 한 쌍으로 이루어진 자료 구조

#특징
# - 중괄호{} 사용
# - 값 변경(수정,삭제,추가) 가능
# - 키(key)는 중복 불가, 값(value)은 중복 허용

person= {
    # key : value
    "name": "엄휘찬",
    "age": 24,
    "phone" : "010-4567-1234",
    "subject" : ["python", "java"]
}

print(person["name"])
person["phone"] = "010-1234-5678" # phone이라는 키를 가진 값을 변경
print(person["phone"])

person["addr"] = "인천 부평구" # 키가 존재하지 않으면 요소를 추가
print(person)

del person["age"] # age라는 키를 가진 요소를 삭제
print(person)

print(person.get("name")) # key가 없으면 None을 반환
print(person["name"]) # key가 없으면 Error를 출력

# x.keys()
# - 모든 key 추출
print(person.keys())

for key in person.keys():
    print(f"꺼낸 키 : {key}")
    print(f"값 꺼내기 : {person[key]}")
    print("--------------------------")

# 딕셔너리.values()
# - 모든 value 추출
print(person.values())

for value in person.values():
    print(f"값 : {value}")

# 딕셔너리.items()
# - key : value를 한 쌍으로 같이 가져옴

print(person.items())

for item in person.items():
    print(item)

for key, value in person.items():
    print(f"{key}: {value}")

#for key,_ in person.items(): items()에서 키만 가져오고 싶을 때 _ 사용 value도 똑같음
#   print(key)

print(f"딕셔너리 오릉차순 정렬 : {sorted(person)}")
print(f"딕셔너리 내릉차순 정렬 : {sorted(person,reverse = True)}")

