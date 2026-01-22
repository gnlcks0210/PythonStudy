try:
    print("프린터 사용을 시작합니다.")
    num = int(input("출력할 페이지 수를 입력하세요: "))
    if num <= 0:
        print("페이지 수는 1 이상이여야 합니다.")
    else:
        print(f"{num}페이지를 출력합니다.")
except ValueError as e:
    print("숫자만 입력해야합니다. 출력이 취소되었습니다.")
    print("발생한 에러 :",e)
finally:
    print("프린터 사용을 종료합니다.")