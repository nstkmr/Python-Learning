ch = input("Enter your character: ")

if(ch >= 'A' and ch <= 'Z'):
    ch = ch.lower()
    print("The entered character is in uppercase. In lowercase it is: "+ str(ch))

else:
    ch = ch.upper()
    print("The entered character is in lowercase. In upeprcase it is: "+ str(ch))