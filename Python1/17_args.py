# 가변길이 매개변수
# - 함수에서 매개변수의 개수를 유연하게 받을 수 있는 기능
# - 항상 맨 뒤에 선언되어야 함

def add(*args):
    print(args)
    return sum(args)
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))

def get_numbers(num1, num2, *numbers):
    print(f"num1 : {num1}")
    print(f"num2 : {num2}")
    print(f"numbers : {numbers}")

print(get_numbers(1,2,3))
print(get_numbers(1,2,3,4))

a = (1)
b = (2,)
c = 1,
d = 1,2,3
print(type(a)) # ,가 없기 때문에 int로 인식
print(type(b))
print(type(c))
print(type(d))

# 패킹 (Packing)
# - 여러 개의 값을 하나의 변수(튜플 등)로 묶는 것을 패킹이라고 부름
def sum_numbers(*numbers): # 패킹
    return sum(numbers)

print(sum_numbers(1,2,3,4))

#언패킹(Unpacking)
# - 묶여있는 값을 풀어서 사용하는 것을 언패킹이라고 부름

# 패킹과 언패킹은 사용 위치에 따라 다르기 때문에 기억해두면 좋음
def max_num(*numbers):
    print("언패킹 : ",*numbers)
    return max(numbers)

print(max_num(1,2,3,4))

tup = (1,2,3,4)

print(*tup) # 언패킹

# 딕셔너리로 가변길이 매개변수 받기
person = {"name":"김재섭", "age":20, "hobby":"coding"}

#키워드 인자를 개수 상관없이 딕셔너리로 패킹
def introduce(**kwargs): # 패킹
    #print(**kwargs)
    pass

introduce(**person) # 언패킹
introduce(name="김재섭", age=20, hobby="coding")

# 키워드 인자
# - 순서 상관없이 매개변수 이름과 일치하는 곳에 데이터를 전달
def introduce2(hobby, age, name):
    print(hobby, age, name)

introduce2("coding",20,"김재섭") # 기본방식
introduce2(name="김재섭", age=20, hobby="coding") # 키워드 인자


def call(name,*args,**kwargs):
    # *args : 위치 인자들을 튜플로 패킹
    # **kwargs : 키워드 인자들을 딕셔너리로 패킹
    print("name : ", name)
    print("args : ", args)
    print("kwargs : " , kwargs)

call("svae",1,2,mode="save_mode",retry=False)


# 1. 첫번째 매개변수는 기준 점수, 나머지는 비교 대상 점수
# - 기준 이상인 값만 출력
def filter_score(base_score,*args):
    for score in args:
        if base_score <= score:
            print(score)

filter_score(60, 10,20,60,80)

# 2. 아래의 딕셔너리를 함수에 전달하고 출력
# - 출력 형식은 key : value
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

data = {"name" : "홍길동" , "age" : 19}
# **data 언패킹의 결과 name="홍길동", age=19
print_info(**data) # == print_info(name="홍길동", age=19)



a , b = (1, 2)
print(a)
print(b)

data = {"a": 1, "b": 2}
x, y= data
print(x)
print(y)

x, y = data.values()
print(x)
print(y)

#------------------------------------------------------------------------
# 위치 인자 패킹(*args)
# - 여러 개의 위치 인자를 튜플로 묶어서 받음

# 키워드 인자 패킹(**kwargs)
# - 여러 개의 키워드 인자를 딕셔너리로 묶어서 받음

# 그 외 매개변수 위치가 아니면 대부분 다 언패킹