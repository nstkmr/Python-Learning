num = int(input("Enter your number: "))
s = 0.0
for i in range(1,num+1):
    a = i / (i+1)
    s = s + a

print("Sum of series 1,2/3,3/4,...,n/(n+1) for n =",num,"is",s)