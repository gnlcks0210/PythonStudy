# 코드를 통해서 hello.txt. 라는 메모 파일을 만들것이다.
# hello.txt 라는 파일을 코드로 읽고 출력을 할 것이다.
from pathlib import Path

#파일의 이름
p = Path("hello.txt")

# 파일을 만들고, 안에 글자를 입력해서 저장하기
with p.open(mode = "w", encoding="utf-8") as f:
    f.write("파이썬 파일 시스템 배워보기")

# mode="w"는 p.open을 쓰기모드로 하겠다.(write)

# 파일을 읽어서 출력하겟다.
with p.open(mode = "r", encoding="utf-8") as f:
    text = f.read()
    print(text)

# 코드를 통해서 텍스트 파일을 만들고, 그 안에 문자를 입력하고 저장한다. 그리고 읽어온다.