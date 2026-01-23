#random에 대한 import
import random

def pick_todo(todos):
    return random.choice(todos)

todo_list = []

for i in range(1,6):
    todo = input(f"오늘 할 일을 입력하세요 ({i}/5)")
    todo_list.append(todo)

print("\n오늘 해야 할 일 목록 : ",todo_list)

today_todo = pick_todo(todo_list)
print("오늘 할 일은 : ", today_todo)