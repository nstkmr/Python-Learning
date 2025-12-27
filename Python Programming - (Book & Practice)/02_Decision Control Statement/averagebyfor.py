n = int(input("Enter your number: "))
avg = 0.0
i = s = 0
for i in range(1,1+n):
    s = s + i
avg = s / i
print("Average of the numbers is: "+ str(avg))