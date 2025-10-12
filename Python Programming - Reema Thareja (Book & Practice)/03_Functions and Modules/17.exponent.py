def exp(a,b):
    if (b==0):
        return 1
    else:
        return a * exp(a,b-1)
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
    
print("Exponent of (", a, ",", b,") is: ", exp(a,b)) 