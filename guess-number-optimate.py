# 30401 王O成 猜數字遊戲
from random import random, randrange, randint
from math import log
from asyncio import run


# 隨機生成上限值目標書字
async def gen_goal():
    
    global top, goal

    top = int(10**random()+randint(randrange(100, 500), randrange(1000, 1500))%1000)

    goal = int(10**random()+randint(randrange(100, 500), randrange(1000, 1500)))

    while goal > top:

        goal = int(goal%top)


# 數字猜測判斷與回應
async def guess():

    global times, inp, max_times, l_range, r_range

    if l_range > inp or r_range < inp:

        return 400

    if inp == goal:

        return 200
    
    elif inp > goal:

        r_range = inp
        print(f"The goal is lower than {inp}...")
        print(f"You have {max_times - times} times left.")
        return 404
    
    elif inp < goal:

        l_range = inp
        print(f"The goal is higher than {inp}...")
        print(f"You have {max_times - times} times left.")
        return 404


# 主程式
if __name__ == "__main__":
    
    run(gen_goal())
    
    global times, inp, max_times, l_range, r_range, waste
    l_range = 1
    r_range = top
    times = 1
    waste = 0
    max_times = int(log(top, 2))+1

    print(f"You have {max_times} times to reach the goal number :D")

    # 次數內重複猜測&判斷
    while times <= max_times:

        inp = int(input(f"Guess a number between {l_range} ~ {r_range}\n> "))

        response = run(guess())

        if response == 200:
            
            print(f"Congraduation ! The goal number is {goal}.")
            print(f"You make a good job making {times} times to get the number.")
            print(f"(include {waste} waste times)")
            quit()
        
        elif response == 400:

            waste += 1
            print(f"You waste one chance to reach the goal :(")
            print(f"You have {max_times - times} times left.")

        times +=1
        
    print(f"Ohhh... The goal is {goal}.")
    print(f"You spend {times-1} times to guess the number. Try it again.")
    print(f"(include {waste} waste times)")