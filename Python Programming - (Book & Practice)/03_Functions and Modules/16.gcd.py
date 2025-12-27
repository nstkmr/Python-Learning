def gcd(a,b):
    rem = a % b
    if(rem==0):
        return b
    else:
       return gcd(b,rem)
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
    
print("GCD of", a,"and", b,"is: ", gcd(a,b))
