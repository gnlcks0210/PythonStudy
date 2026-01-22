try:
    count = int(input("신청할 강의 수를 입력하세요: "))

    if count <= 0 :
        raise ValueError("수강 강의 수는 1이상이어야 합니다.")
    print(f"{count}강의를 신청했습니다.")
except ValueError as e:
    print(e)