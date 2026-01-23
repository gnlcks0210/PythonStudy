# 다른 파일에 있는 기능을 가져오기 위해서는 import를 해야한다.
# 파일에 가장 위에다가 적어주면 된다.
from TimeModule import hour_to_min
from TimeModule import hour_to_sec
from TimeModule import min_to_sec
# import TimeModule



min = hour_to_min(6)
print(f"6시간은 {min}분 입니다.")

# min = TimeModule.hour_to_min(6)
# print(f"6시간은 {min}분 입니다.")
#
#
# # 12분을 초로 바꿔서 출력해보기
# sec = TimeModule.min_to_sec(12)
# print(f"12분은 {sec}초 입니다.")
#
# # 3시간을 초로 바꿔서 출력해보기
# sec = TimeModule.hour_to_sec(3)
# print(f"3시간은 {sec}초 입니다.")