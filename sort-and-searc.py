# global

val={}

# sort func_

def sort():
    for x in range(int(len(val))-1):
        for y in range(x+1,int(len(val))):
            # print(y)
            if val[x]>val[y]:
                tmp=val[x]
                val[x]=val[y]
                val[y]=tmp
    print(val)

#search func_

def search(g, l, r):
    mid=int((l+r)/2)
    
    if l>r:
        print('err0r')
        return
    
    elif val[mid] is g:
        print(f'index:{mid}')
        return
        
    elif val[mid]<g:
        search(g, mid+1, r)
        
    else:
        search(g, l, mid-1)

# main
n=int(input('input how many numbers in the array?\n> '))
print('input')
for i in range(n):
    val[i]=int(input(f'{i+1}. '))

sort()

m=int(input('input how many numbers need to search?\n> '))
print('input')

for i in range(m):
    tmp=int(input(f'{m}. '))
    search(tmp, 0, int(len(val))-1)
