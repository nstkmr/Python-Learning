m = m1 = int(input("Enter the value of m: ")) # Here i have assigned value to another variable m1 to print it at the last
n = int(input("Enter the value of n: "))
s = 0
while(m<=n):
    s = s + m
    m = m + 1
print("The sum from "+ str(m1) +" to "+ str(n) +" is: "+ str(s))