n = int(input("Enter your number: "))

i = 0
s = 0
while(i<=n):
    s = s + i
    i = i + 1

avg = float(s)/10
print("The average of first 10 number is: "+ str(avg))
print("The sum of first 10 number is: "+ str(s))