# 시간을 변환해주는 기능을 만들것이다.
# 변수 : 항상 변할 수 있는 값
# 상수 : 변하지 않는 값
#      ㄴ분, 시, 초 60분,60초 1시간, 파이 3.14........
# 상수 선언할 때는 암묵적인 관례, 네이밍 = 대문자 혹은 스네이크케이스
# 상수는 대문자로 선언 MIN = 10
# 스네이크케이스  board list -> BOARD_LIST

MIN = 60
SEC = 60

# 3개의 함수(메소드)를 만들겠다.
# 다른곳에서도 사용가능한 메소드

# 매개변수로 시간이 들어오면 분 단위로 변환 후 반환
def hour_to_min(hour):
    return hour * MIN

# 매개변수로 분이 들어오면 초 단위로 변환 후 반환
def min_to_sec(min):
    return min * SEC

# 매개변수로 시간이 들어오면 초 단위로 변환 후 반환
def hour_to_sec(hour):
    return min_to_sec(hour_to_min(hour))

# hour_to_sec 를 실행하게되면
# 1. 다른파일에서 hour_to_sec를 실행한다. 시간은 1시간을 보냈다.
# 2. hour_to_min이 먼저 실행한다. 60반환
# 3. min_to_sec가 실행한다. 매개변수는 60이다.
# 4. 60 * 60 = 3600을 반환
# 5. hour_to_sec를 호출한 다른파일에 3600이라는 값을 보내준다.