num = int(input("Enter your number: "))
n = int(input("Enter your power value: "))

result = 1 
for i in range (n):
    result= result * num

print(num,"raise to the power",n,"is",result)