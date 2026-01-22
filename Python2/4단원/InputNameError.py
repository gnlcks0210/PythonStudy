#사용자 정의 예외 클래스
class InputNameError(Exception):
    pass

# 이름에 숫자가 포함되어 있는지 확인하는 함수
def is_there_digit(name):
    #반복문을 사용
    for ch in name:
        if ch.isdigit():
            return True
    return False

try:
    name = input("이름을 입력해주세요: ")
    if is_there_digit(name):
        raise InputNameError("사람의 이름에는 숫자가 들어갈 수 없습니다.")
    print(f"{name}님 어서오세요.")
except InputNameError as e:
    print(f"예외 발생 : {e}")

finally:
    print("프로그램을 종료합니다.")