positives = negatives = zeroes = 0
print("Enter -1 to exit...")
while(1):
    num = int(input("Enter a number: "))
    if(num == -1):
        break
    elif(num > 0):
        positives += 1

    elif(num < 0):
        negatives += 1

    else:
        zeroes += 1

print("The number of positives entered: "+ str(positives))
print("The number of negatives entered: "+ str(negatives))
print("The number of zeres entered: "+ str(zeroes))
