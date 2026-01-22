try:
    number_list = [1,2,3,4]
    print(number_list[5])

except IndexError as e:
    print("인덱스 범위를 벗어났습니다.")
    print("발생한 예외는",e,"입니다.")
