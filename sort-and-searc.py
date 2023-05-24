from asyncio import run
# sort func_

async def sort():
    for x in range(int(len(val))-1):
        for y in range(x+1,int(len(val))):
            # print(y)
            if val[x]>val[y]:
                val[x], val[y] = val[y], val[x]
    print(val)

#search func_

async def search(g, l, r):
    
    mid = int((l+r)/2)
    
    if l > r:
        
        print('404 Not Founded')
        return
    
    elif val[mid] == g:
        
        print(f'index:{mid}')
        return
        
    elif val[mid] < g:
        
        await search(g, mid+1, r)
        
    else:
        
        await search(g, l, mid-1)

# main
if __name__ == "__main__":
    
    global val
    val = {}
    n=int(input('input how many numbers in the array?\n> '))
    print('*input*')
    for i in range(n):
        val[i]=int(input(f'{i+1}. '))
    
    run(sort())
    
    m=int(input('input how many numbers need to search?\n> '))
    print('*input*')
    
    for i in range(m):
        tmp=int(input(f'{i+1}. '))
        run(search(tmp, 0, int(len(val))))
        
    print("Process Ended.")
