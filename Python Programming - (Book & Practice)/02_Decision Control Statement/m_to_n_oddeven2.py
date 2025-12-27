m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

if(m%2==0):
    for i in range (m,n+1,2):
        print(i,"is even number")
    for i in range (m+1,n+1,2):
        print(i,"is odd number")
    
    
else:
    for i in range (m,n+1,2):
        print(i,"is odd number")
    for i in range (m+1,n+1,2):
        print(i,"is even number")