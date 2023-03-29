from random import random, randrange, randint
from math import log
from asyncio import run


# 隨機生成上限值目標書字
async def gen_goal():
    
    global top, goal

    top = int(10**random()+randint(randrange(100, 500), randrange(1000, 1500))%1000)

    print(f"The range of this game is 1 ~ {top}")

    goal = int(10**random()+randint(randrange(100, 500), randrange(1000, 1500)))

    print(goal)

    while goal > top:

        goal = int(goal%top)


# 數字猜測判斷與回應
async def guess():

    global times, inp, max_times

    if inp == goal:

        return 200
    
    elif inp > goal:

        print(f"The goal is lower than {inp}...")
        print(f"There are {max_times - times} times left.")
        return 404
    
    elif inp < goal:
        print(f"The goal is higher than {inp}...")
        print(f"There are {max_times - times} times left.")
        return 404


# 主程式
if __name__ == "__main__":
    
    run(gen_goal())
    
    global times, inp, max_times
    times = 1
    max_times = int(log(top, 2))+1

    # 次數內重複猜測&判斷
    while times < max_times:

        inp = int(input("Guess a number\n> "))

        response = run(guess())

        if response == 200:
            
            print(f"Congraduation ! The number is {goal}.")
            print(f"You make a good job making {times} times to get the number.")
            quit()
        
        times +=1
        
    print(f"Ohhh... The goal is {goal}.")
    print(f"You spend {times} times to guess the number. Try it again.")