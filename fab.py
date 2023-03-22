a = [1, 1]

def fab(n):

    if n == 0:
        return 0
    #if n == 1 or n == 2 :
        
    #   return 1

    if len(a) <= n:
        
        a.append(fab(n-1)+fab(n-2))
        a.sort()
        return a[len(a)-1]
        
    return a[n]

while(True):

    i = int(input("Your stage number(-1 to break)\n> "))
    if i == -1:
        print("Good Bye :D")
        break
    print(fab(i))
