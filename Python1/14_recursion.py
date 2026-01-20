# 재귀호출
# - 자기 자신을 다시 호출하는 방식

# 참고
# - 일반적으로 실무에서 코드 작성할때는 거의 사용되지 않음
# - 코딩 테스트, 정보처리기사 문제 풀이에 많이 나옴

# 안쓰이는 이유
# - 메모리 낭비가 심함
# - 가도성 엄청 안좋음, 디버깅도 어려움

def countdown(n):
    if n == 0 :
        print("발사!")
        return
    print(n)
    countdown(n - 1) # 재귀 호출

countdown(5)

# 1부터 3까지 숫자를 더하는 재귀호출
def add_numbers(n):
    if n == 0:
        return 0
    return n + add_numbers(n-1)
    #순서
    # 1. 처음 호출 시  n = 3
    # 2. if문은 3 == 0: -> False
    # 3. return 3 + add_numbers(3-1)
    # 4. (두 번재 호출)
    # 5. n = 2
    # 6. if문은 2 == 0: -> False
    # 7. return 2 + add_numbers(2-1)
    # 8. (세 번째 호출)
    # 9. n = 2
    # 10. if문은 1 == 0: -> False
    # 11. return 1 + add_numbers(1-1)
    # 12. (네 번째 호출)
    # 13. n = 0
    # 14. if문은 0 == 0: -> True
    # 15. return 0

print(add_numbers(3))