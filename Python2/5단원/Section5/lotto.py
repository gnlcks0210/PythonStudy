# random 내장 모듈 import
import random

# 함수를 하나 만들도록 하겠습니다.
def generate_lotto():
    lotto = random.sample(range(1,45), k=6)
    return lotto

lotto_numbers = generate_lotto()
print(f"이번주 로또 번호는 ? {sorted(lotto_numbers)}")