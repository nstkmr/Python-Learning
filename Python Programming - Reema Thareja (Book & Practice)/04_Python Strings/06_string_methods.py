str1 = "i am nishant kumar and i like to code"
print(str1.capitalize()) # This method capitalize the first letter

str2 = "Hello"
print(str2.center(10,' ')) # This method centralize any sentence or word with using * or null character

str3 = "Hello"
print(str3.ljust(10,'*')) # This method add * at the left side to make the srting of length 10

str4 = "Hello"
print(str4.rjust(10,'*')) # This method add * at the right side to make the srting of length 10

message1 = "Are you fucking retarded or something, who the fuck uses 200ml of petrol to cook a fucking vegetable, this make no fucking sense"
str5 = "fucking"
print(message1.count(str5,0,len(message1)))

message2 = "O hell nah bro! shit! I aint doing no shit"
print(message2.endswith('shit',0,len(message2)))
print(message2.startswith('O',0,len(message2)))
print(message2.find('aint',0,len(message2)))
# print(message2.index('z',0,len(message2))) # This is same as find method but it'll will throw an error/raises an exception that substring is not found
print(message2.rfind('shit',0,len(message2))) # This will use the same 0 1 2 3 index to find but will go from the end to start 
# print(message2.rindex('z',0,len(message2))) # This also as above 