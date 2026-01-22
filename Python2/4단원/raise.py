try:
    # 나이에 대한 변수를 입력 받겠다.(정수형)
    age = int(input("나이를 입력해주세요 : "))
    # 조건: 1살 미만 또는 200살 초과할 경우 오류를 발생시키겠다.
    if age < 1 or age > 200:
        # raise : 예외를 발생시킨다.
        raise ValueError("나이는 1살 이상 200이하로 입력해주세요.")
    else:
        print(f"당신의 나이는 {age}살 이시군요!")
except Exception as e:
    print("예외 메시지 :",e)
finally:
    print("프로그램을 종료합니다.")