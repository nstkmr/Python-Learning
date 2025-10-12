str1 = "{}, {} and {}".format('Sun','Moon','Stars') # Here the curly brackets{} replaced by the given argument
print("The default sequence of arguments is: " + str1)

str2 = "{1}, {0} and {2}".format('Sun','Moon','Stars') # Here we can also specify the position as we want to replace
print("The positional sequence of arguments (1,0,2) is: " + str2)

str3 = "{c}, {b} and {a}".format(a='Sun',b='Moon',c='Stars') # Here also
print("The keyword sequence of arguments is: " + str3)
