temp = int(input("Enter a temperature: "))
char= input("Enter C or F: ")
if char == "C" or "c" :
    F= (9/5 * temp) + 32
    print(temp,"°C is", F, "°F")
elif char == "F" or "f" :
    C = (temp-32) * (5/9)
    print(temp,"°F is", F, "°C")