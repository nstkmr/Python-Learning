num = int(input("Enter your number: "))
s = 0.0
for i in range(1,num+1):
    a = i**3
    s = s + a

print("Sum of cubes 1,2^3,3^3,...,n^3 for n =",num,"is",s)