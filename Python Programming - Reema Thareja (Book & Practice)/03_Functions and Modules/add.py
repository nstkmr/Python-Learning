import sys

if len(sys.argv) == 3:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    total = int(num1) + int(num2)
    print("The sum is " + str(total))
else:
    print("Please type: python add.py number1 number2")