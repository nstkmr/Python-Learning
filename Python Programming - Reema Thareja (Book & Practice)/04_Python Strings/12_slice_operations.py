str1 = "NISHANT"
print("str[1:5] = ", str1[1:5])
print("str[0:6] = ", str1[:6]) # This will starts from the start
print("str[1:6] = ", str1[1:]) # This will go to the end of string and also print the last character like len(str1)
print("str[0:7] = ", str1[0:len(str1)])
print("str[0:20] = ", str1[0:20]) # If the provided index is larger than the length of the string then it prints till the last character (ie len(str1))

str2 = "PYTHON"
print("str[-1] = ", str1[-1]) # It can also be accessed using negative index
print("str[-7] = ", str1[-7])
print("str[-7:-4] = ", str1[-7:-4])

str3 = "NishantKumar"
print("str[1:5:1] = ", str1[1:5:1]) # We can also specify the stride, like how many characters it'll jump (Here it'll not jump)
print("str[1:5:2] = ", str1[1:5:2]) # Here it'll jump 1 character
print("str[1:6:3] = ", str1[1:6:3]) # Here it'll jump 2 characters
print("str[::3] = ", str1[::3])