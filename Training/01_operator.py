# 점수(score)는 75점이고 출석률(attendace) 80인 학생이 있습니다
# 학생의 점수가 60점 이상이고, 출석률이 80이상이면 result 변수에 True 할당
score = 75
attendance = 80
result = score >= 60 and attendance >= 80
print(result)

# 키가 165이고, 나이가 9세인 아이가 있습니다.
# 키(height)가 150 초과이고, 나이가 10세 이상이면 result 변수에 True 할당
height = 165
age = 9
result = height > 150 and age >=10
print(result)

# 현제 비가 오지 않고, 기온은 12도 입니다.
# 비가 오지 않고(is_raining) 기온(temperature)이 10도 이상이면 True 할당
is_raining = False
temperature = 12
result = not is_raining and temperature >= 10

print(result)

# 온라인 출석(online_attendance)을 한 학생이 있습니다. (True)
#   > 온라인 출석을 했기 때문에 오프라인 출석은 False
# 온라인 출석을 했거나 오프라인 출석(offline_attendance)을 했다면
# 수업 참여가 인정됩니다. (result에 True 할당)
online_attendance = True
offline_attendance = False
result = online_attendance or offline_attendance

print(result)