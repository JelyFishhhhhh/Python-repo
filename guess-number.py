from random import random, randrange
from math import sqrt

def guess():
    # 目標數字
    global goal, inp, times
    goal = int(random()*randrange(2, 10)**randrange(2, 10))
    # 輸入上標值
    top = int(input("請輸入上限值"))
    # 調整目標數字
    while goal > top:
        goal = int(goal%top) **2
    
    # 起始值設置
    inp = -1
    times = 1
    
    # 猜數字
    while times <= int(sqrt(top)):

        inp = input("Guess a number")
        if  inp == goal:
            break
        print(f"Ur Wrong! you have {int(sqrt(top)) - times} time(s) left :)")
        times += 1

guess()

# 判斷
if inp == goal:
    print(f"Congraduation ! The number is {goal}.")
    print(f"You make a good job making {times} times to get the number.")
    
else:
    print(f"The number is {goal}. Try it again :)")
    guess()
