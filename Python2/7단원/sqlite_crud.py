import sqlite3

#DB_PATH = 현재 경로(7단원 까지의 경로 + app.db 파일 이름까지 변수에 저장)
DB_PATH = "app.db"

# DB를 생성하는 함수
def init_db():
    #sqllite를 연결 conn : connect약자
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            #데이터 베이스의 SQL문이 들어갈자리
            #ex) CREATE, INSERT, SELECT
            #테이블 만들기
            """
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    email TEXT UNIQUE
                );
            """
        )
        conn.commit()
        print("DB. 초기화 완료 ( 테이블 : users )")
    finally:
        conn.close()

# 메인함수

def main():
    # 테이블이 없으면 app.db를 생성
    init_db()

    while True:
        print("\n ====SQLITE CRUD ( 단일 파일 )====")
        #0~5까지 메뉴 만들기
        print("1) 사용자 추가 (Create)")
        print("2) 전체 목록 (Read)")
        print("3) 이름 검색 (Read)")
        print("4) 정보 수정 (Update)")
        print("5) 사용자 삭제 (Delete)")
        print("0) 프로그램 종료")
        choice = input("번호 선택 :").strip()

        if choice == "1":
            #사용자를 추가하는 함수
            create_user()
        elif choice == "2":
            #사용자를 목록으로 출력해주는 함수
            list_user()
        elif choice == "3":
            # 사용자의 이름을 바탕으로 찾아주는 함수
            find_user()
        elif choice == "4":
            # 사용자의 id를 기준으로 값을 수정해주는 함수
            update_user()
        elif choice == "5":
            # 사용자의 id를 기준으로 삭제해주는 함수
            delete_user()
        elif choice == "0":
            print("안녕히 가세요")
            break # while문 종료
        else:
            print("올바른 번호를 입력하세요")

# --------------------- C : Create ---------------------
#유저를 추가하는 함수
def create_user():
    name = input("이름 : ")
    age_text = input("나이(숫자, 생략 가능) : ")
    email = input("이메일(중복 불가, 생략 가능) : ")

    #age_text를 숫자형으로 형 변환
    age = int(age_text) if age_text.isdigit() else None

    #DB 연결
    conn = sqlite3.connect(DB_PATH)

    # 예외처리
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users(name, age, email) VALUES (?, ?, ?)",
            (name, age, email)
        )
        #내용 저장/변경사항 적용
        conn.commit()
        print("사용자 정리 완료")
    except sqlite3.IntegrityError:
        print("이메일이 중복 됩니다. 다른 이메일을 사용하세요.")
    finally:
        conn.close()


# --------------------- R : Create ---------------------
#데이터를 읽어오는 함수
def list_user():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        #ORDER BY 오름차순
        #ORDER BY DESC 내림차순
        cur.execute("SELECT id, name, age, email FROM users ORDER BY id")
        rows = cur.fetchall() # 검색 결과 모두 가져오기

        if not rows:
            print("(비어있음)")
            return
        print("\n[사용자 목록]")
        for r in rows:
            print(f"- id={r[0]} | name={r[1]} | age={r[2]} | email={r[3]}")
    finally:
        conn.close()

# --------------------- R : Read ---------------------
def find_user():
    keyword = input("이름(부분 일치) 검색어 : ").strip()
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, age ,email FROM users WHERE name LIKE ? ORDER BY id",
                    (f"%{keyword}%", ),
        )
        conn.commit()

        rows = cur.fetchall()
        if not rows:
            print("결과가 없습니다.")
            return
        print("\n[사용자 목록]")
        for r in rows:
            print(f"- id={r[0]} | name={r[1]} | age={r[2]} | email={r[3]}")
    finally:
        conn.close()
# --------------------- U : Update ---------------------
#기존에 데이터를 수정하는 함수(데이터 추가 x)
def update_user():
    #고유성 때문에 id로 찾는다.
    #name은 중첩이 될 수 있으니 사용 x
    id_text = input("수정할 사용자 id : ")

    uid = int(id_text)
    new_name = input("새 이름(엔터 = 변경 안 함): ")
    new_age = input("새 나이(숫자, 엔터 = 변경 안 함): ")
    new_email = input("새 이메일(엔터 = 변경 안 함): ")

    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE users 
            SET name = ?,
                age = ?,
                email = ?
            WHERE id = ?
            """,
            (new_name, new_age, new_email,uid)

        )
        conn.commit()
        print("수정 완료")
    except sqlite3.IntegrityError:
        print("이메일이 중복 됩니다. 다른 이메일을 사용하세요")
    finally:
        conn.close()
# --------------------- D : Delete ---------------------
def delete_user():
    id_text = input("삭제할 사용자 아이디: ")
    uid = int(id_text)
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = ?", (uid,))
        # 입력한 id가 없을경우
        # rowcount -> 몇 가지의 데이터가 변했냐 rowcount로 확인할 수 있다.
        # 삭제가 이루어지면 rowcount == 1 아니면 0
        if cur.rowcount == 0:
            print("해당 id의 사용자가 없습니다.")
        else:
            conn.commit()
            print("삭제 완료!")

    finally:
        conn.close()


# 이 파일을 실행할때 main 을 실행시킴
if __name__ == "__main__":
    main()


