num = int(input("Enter your number: "))
s = 0.0
for i in range(1,num+1):
    a = 1 / (i**2)
    s = s + a

print("Sum of series 1,1/2^2,1/3^2,...,1/n^2 for n =",num,"is",s)