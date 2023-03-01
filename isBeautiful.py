import math
num = int(input('Is this number beautiful?\n> '))

total = 1

for x in range(2, int(math.sqrt(num))+2):
    if not num % x:
        total *= x

if total == num:
    print(f'{num} is beautiful.')
    
else:
    print(f'{num} is ugly.')
