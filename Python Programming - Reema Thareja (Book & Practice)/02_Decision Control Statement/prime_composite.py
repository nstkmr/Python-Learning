number = int(input("Enter number: "))
composite = 0

if (number<2):
    print("The number is neither prime nor composite")

else:

    for i in range(2, number): # It checks for number-1 iteration starting from 2 (means other than 1 or itself)
        if (number % i == 0):
            composite = 1
            break

    if composite == 1:
        print("Number is Composite")
        
    else:
        print("Number is Prime")