from pathlib import Path


filename = input("파일의 이름을 입력하세요 : ")
p = Path(filename)
name = input("이름을 입력하세요 : ")
with p.open(mode = "w", encoding = "utf-8") as f:
    f.write("파이썬 파일 시스템 배워보기\n")
    f.write(f"이름 : {name}")

with p.open(mode = "r", encoding = "utf-8") as f:
    text = f.read()
    print(text)

