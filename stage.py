a = [1]

def stage(n):

    if n == 0:
        return 1

    if len(a) <= n:
        a.append(n*stage(n-1))
        a.sort()
        return a[len(a)-1]
        
    return a[n]

while(True):

    i = int(input("Your stage number(-1 to break)\n> "))
    if i == -1:
        print("Good Bye :D")
        break
    print(stage(i))
