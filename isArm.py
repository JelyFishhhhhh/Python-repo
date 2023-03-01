n,m = map(int,input('Input a range to check armstrong number?\n> ').split())
lis = []

for i in range(n, m+1):
    total = 0
    for x in str(i):
        total += int(x) ** len(str(i))
        
    if total == i:
        lis.append(int(i))

# 空集合(X
if not len(lis):
    print('There are no armstrong number between this range "(', end = '')

# print armstrong list in range
else:
    print('These number are armstrong number between this range\n> ', end = '')
    for i in lis:
        print(i, end = '')
        if i is not lis[-1]:
            print(', ', end = '')
            
print()
