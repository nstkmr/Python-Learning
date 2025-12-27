str1 = "1234"
print(str1.zfill(10)) # This will add zeroes on the left side of string to make it the length of 10

str2 = "Hello"
print(str2.lower()) # This will write the string in lower case 
print(str2.upper()) # This will write the string in upper case 

str3 = "    Hello"
print(str3.lstrip()) # It will remove all the leading whitespaces 

str4 = "    Hello     "
print(str4.rstrip()) # It will remove all the trailing whitespaces

str5 = "    Hello     "
print(str5.strip()) # It will remove all the whitespaces

str6 = "AaBbKkZz"
print(max(str6)) # It will return the highest alphabatical character according to 
print(min(str6)) # It will return the maximum 