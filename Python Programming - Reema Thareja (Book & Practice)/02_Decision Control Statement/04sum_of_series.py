num = int(input("Enter your number: "))
s = 0.0
for i in range(1,num+1):
    a = (i**i) / i
    s = s + a

print("Sum of series 1,2^2/2,3^3/3,...,n^n/n for n =",num,"is",s)