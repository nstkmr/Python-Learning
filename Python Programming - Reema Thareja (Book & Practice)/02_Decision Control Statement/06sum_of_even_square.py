num = int(input("Enter your number: "))
s = 0.0
for i in range(1,num+1):
    if(i%2==0):
        a = i**2
        s = s + a

print("Sum of even squares 2^2,4^2,...,2n^2 for n =",num,"is",s)