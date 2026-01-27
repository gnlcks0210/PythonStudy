from pathlib import Path

# 실습용 폴더
base_cwd = Path.cwd()
base = base_cwd /"file_mode_lab"
base.mkdir(exist_ok = True)

# 출력용 함수
def line(title):
    print("\n" + "=" *60)
    print(f"[ {title} ]")
    print("=" * 60)

# 1. "r" : 읽기 모드
# p_r = base / "mode_r.txt"
# p_r.write_text("읽기 모드 테스트\n두 번째 줄", encoding = "utf-8")
#
# line("1. 'r' 읽기모드")
#
# try:
#     with p_r.open(mode = 'r',encoding = "utf-8") as f:
#         print("파일 내용 :\n",f.read())
# except FileNotFoundError:
#     print("파일이 존재하지 않습니다.")

# 2. 'w' : 쓰기 모드(기존 내용 초기화)
# p_w = base / "mode_w.txt"
# line("2. 'w' 쓰기모드")
#
# with p_w.open(mode = "w",encoding = "utf-8") as f:
#     f.write("첫 번째 작성\n")
#
# print("첫 번재 작성 완료")
#
# # 덮어쓰기
# with p_w.open(mode = "w",encoding = "utf-8") as f:
#     f.write("두 번째 작성\n")
#
# print("두 번째 작성 완료")

# 3. 'a' : 이어쓰기 모드
# 파일이 없으면 생성 파일이 있으면 커서가 끝으로 이동해서 이어서 작성가능
# p_a = base / "mode_a.txt"
# line("3. 'a' 이어쓰기 모드")
#
# with p_a.open(mode = "a", encoding = "utf-8") as f:
#     f.write("첫 번째 작성\n")
#
# with p_a.open(mode = "a", encoding = "utf-8") as f:
#     f.write("두 번째 작성\n")
#
# with p_a.open(mode = "r", encoding = "utf-8") as f:
#     print(f.read())

# 4. 'x' : 새로 만들기 전용 모드
# 파일이 없을 때 생성 하는 용도이다
# 파일이 있으면 FileExistsError가 발생한다.
# p_x = base / "mode_x.txt"
# line("4. 'x' 새로 만들기 모드")
#
# try:
#     with p_x.open(mode = "x", encoding = "utf-8") as f:
#         f.write("새 파일 작성 완료\n")
#         print("파일 생성 성공!")
# except FileExistsError:
#     print("이미 존재하는 파일입니다.")

# 5. '+' : 조합 모드

p_plus = base / "mode_plus.txt"
line("5. '+' 조합 모드")

# w+,r+,a+ 사용 예시

# w+
with p_plus.open(mode = "w+" ,encoding = "utf-8") as f:
    f.write("hello world!!\n")
    f.seek(0) # 커서의 시작점을 정해주는 함수
    print("w+ 읽기 결과 :",f.read())

# r+
# mode_plus의 내용을 새로 덮어쓰기
p_plus.write_text("ABCDE",encoding = "utf-8")

with p_plus.open(mode = "r+",encoding = "utf-8") as f:
    data = f.read()
    print("r+ 읽기 결과 : ",data)
    f.seek(2)
    f.write("123")
print("r+ 수정 결과 : ",p_plus.read_text(encoding="utf-8"))

# a+
with p_plus.open(mode = "a+",encoding = "utf-8") as f:
    f.write("\n 추가 내용")
    f.seek(0)
    print("a+ 읽기 결과 :\n",f.read())

