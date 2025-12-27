str1 = "Hello"
print("The ID of str is: ",id(str1))
str2 = "World"
str1 += str2
print("Now the str1 is: " + str1)
print("Now the ID of str1 is: ",id(str1)) # Now since we cancatenate str1 its ID will become different b\c of immutable nature 
str3 = str1
print("The str3 is: " + str3)
print("The ID of str1 is: ",id(str3)) # The ID will be the same as of str1 

