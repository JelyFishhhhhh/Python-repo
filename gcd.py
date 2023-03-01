a = int(input("Input the FIRST number:\n> "))
b = int(input("Input the SECOND number:\n> "))

def GCD(a, b):
    tmp = a % b
    if not tmp:
        if b == 1:
            return f"GCD({a}, {b}) = PRIME."
        
        return f"GCD({a}, {b}) = {b}"
    else:
        return GCD(b, tmp)

print(GCD(a, b))
        
            
