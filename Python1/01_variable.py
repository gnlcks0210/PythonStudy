#<주석>
# - 코드가 실행되지 않고 개발자가 메모하는 용도로 사용

#<변수>
# - 어떠한 값(data)을 저장할 수 있는 저장 공간
# - 변수 초기화 : 선언해둔 변수에 값을 할당하는 과정
age = 20

print(age)

#<네이밍 규칙>
# - 영어, 한글, 숫자 사용 가능
# - 대소문자 구분
# - 변수명의  첫 글자를 숫자로 시작할 수 없음
# - 언더바(_)를 제외한 특수 문자 사용 불가
# - 파이썬 예약어 사용 불가

나이 = 10 # 한글 사용 가능
print(10)

# 대소문자 구분
num_1 = 100
Num_1 = 200
print(num_1)
print(Num_1)

# 변수명의 첫 글자를 숫자로 시작할 수 없음
# -> 1_num = 100 (X)

# 언더바(_)를 제외한 특수문자 사용 불가
# -> num@@ = 300 (X)

#파이썬 예약어 사용 불가
# -> break = 100 (X)

name = "Alice"
age = 25
address = "우편번호 12345 서울시 영등포구 여의도동 서울빌딩 555호"
boy_friend = None #데이터가 없음(None)
height = 168.4

print("이름 :",name)
#f_String
print(f"나이 :{age}, 주소: {address}")
#boy_friend, height
#남친 : None, 키 : 168.4
print(f"남친 :{boy_friend}, 키: {height}")

#사용자로부터 값 입력받아서 변수로 저장하기
input_name = input("이름을 작성해주세요 : ")
print(f"입력한 이름은:{input_name} 입니다.")

input_age = input("나이를 작성해주세요 : ")
print(f"입력한 나이는:{input_age} 입니다.")

#<자료형>
# - 데이터의 종류를 구분하는 이름
# - 숫자, 문자열, 참/거짓 등

#<종류>
# 1. 숫자형 ex) num = 100, age = 24
# 2. 논리형 ex) is_true = True, is_false = False
# 3. 문자열 ex) str = "안녕하세요"
# 4. 리스트
# 5. 튜플
# 6. 세트
# 7. 딕셔너리

#<숫자형>
# - 정수형(int)와 실수형(float)으로 나뉘어짐
int_num_1 = 50
int_num_2 = -70
print("int_num_1:",int_num_1)
print("int_num_2:",int_num_2)
print("int_num_1의 타입은", type(int_num_1))
print("int_num_2의 타입은", type(int_num_2))

#type(data)
# -해당 data가 어떠한 자료형을 가졌는지 확인해주는 기능

#<실수형>
# - 소수점이 존재하는 숫자
float_num_1 = 3.14
print("float_num_1:",float_num_1)
print("float_num_1의 타입은 ", type(float_num_1))

#<논리형>
# - 참(True) 또는 거짓(False)를 가지는 자료형
is_student = True
is_false = False

print("is_student의 값은",is_student)
print("is_false의 값은", is_false)
print("is_student의 타입은", type(is_student))

#<문자열>
# - 문자열을 저장하는 자료형
# - 작은 따옴표와 큰 따옴표 둘 다 사용 가능
string_name = "Alice"
string_greeting = 'Hello, Python~'
print("string_name의 값은",string_name)
print("string_greeting의 값은", string_greeting)
print("string_name의 타입은", type(string_name))

#<문자열 함수>
# - 파이썬에서 미리 만들어둔 다양한 내부 기능(함수)들이 존재하는데
#   이 중에서 문자열을 다루는 일부 함수르르 사용한다

#1.문자열.upper()
# - 문자열을 대문자료 변환

text = "Hello.Python!"
print("upper 사용 전 : ", text)
upper_text = text.upper()
print("upper 사용 후 : ",upper_text)

#2.문자열.lower()
# - 문자열을 소문자료 변환

lower_text = text.lower()
print("lower 사용 후 : ",lower_text)

#3. strip()
# - 문자열의 양쪽 공백을 제거
text_2 = "     Hello, Python!      "
print("strip 사용 전 ",text_2 )

strip_text_1 = text_2.strip()
print("strip 사용 후 ",strip_text_1)

text_3 = "********Hello, Python!****************"
strip_text_2 = text_3.strip("*")
print("strip('*') 사용 후 ", strip_text_2)