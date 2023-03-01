p = int(input("Input the FIRST number:\n> "))
q = int(input("Input the SECOND number:\n> "))

def GCD(a, b):
    tmp = a % b
    if not tmp:
        if b == 1:
            return f"GCD({a}, {b}) = PRIME."
        
        return f"GCD({p}, {q}) = {b}"
    else:
        return GCD(b, tmp)

print(GCD(p, q))
        
            
