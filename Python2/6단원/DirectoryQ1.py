from pathlib import Path
import datetime

directory_name = input("폴더 이름을 입력해주세요 : ")
file_name = input("파일 이름을 입력해주세요 : ")

base = Path.cwd()
data_dir = base / directory_name
data_dir.mkdir(exist_ok=True)
file_path = data_dir / file_name

now = datetime.datetime.now()

with file_path.open(mode = "w", encoding = "utf-8") as f:
    f.write(f"파일 생성 시간: {now}")
print("파일 생성 및 저장 완료!")

# 실습 목표
# 1. 파일을 생성하는 방법 익히기
# 2. 폴더를 생성하는 방법 익히기
# 3. datetime.now를 통해서 현재 날짜 및 시간을 가져오기