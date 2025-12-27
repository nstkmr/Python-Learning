str1 = "Duck Duck Duck"
print(str1.replace('Du','Fu')) # It will replace any character or substring from a string

str2 = "It takes as long It takes"
print(str2.title()) # It writes every substring's fisrt character in capital letter
print(str2.swapcase()) # it does opposite of the given string (it writes capital for small letters and vice versa)

str3 = "abc,def, ghi,jkl"
print(str3.split(',')) # It makes a list of substrings separated by comma(,) if given delimiter is comma

str4 = "Hello"
print(str4.isidentifier()) # This checks if the variable is identifier or not
print(list(enumerate(str3))) # This writes pair of every index and character