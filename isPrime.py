import math
inp = int(input('Is this prime?\n> '))
isPrime=True

for i in range(2, int(math.sqrt(inp))+1):
    if inp % i == 0:
        isPrime=False
        break
    
print(f'{inp}  == prime is {isPrime}')
