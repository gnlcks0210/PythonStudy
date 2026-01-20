# break
#  - 반복문을 강제로 종료
count = 0

while count < 10:
    print(count)

    if count == 5:
        break

    count += 1

# continue
#  - 현재 반복을 건너 뛰고 다음 반복으로 이동해주는 키워드
count = 0

while count < 10:
    count += 1

    if count % 2 == 0:
        continue

    print(count)









