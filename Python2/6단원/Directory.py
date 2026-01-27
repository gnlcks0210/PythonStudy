# 현재 코드가 있는 파일 위치 (6단원)에다가 data라는 폴더를 생성한다.
from pathlib import Path

# base(Path.cwd())는 현재 파일의 위치를 가져오는 함수이다.
base = Path.cwd()
# base에다가 하위 폴더를 data라는 이름으로 만들었다.
data_dir = base / "data"
# mkdir이라는 것은 make directory의 약자로서 폴더를 만드는 명령어이다.
data_dir.mkdir(exist_ok=True)
file_path = data_dir / "data.txt"


print(file_path)

