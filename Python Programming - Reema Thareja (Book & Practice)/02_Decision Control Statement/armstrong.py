n = num = int(input("Enter your number: "))
s = 0
while(n>0):
    r = n%10
    s = s + (r**3)
    n = n//10 # The operator // is an floor division, it gives an integer value

if (s == num):
    print("The given number is an armstrong number")

else:
    print("It's not an armstrong number")
