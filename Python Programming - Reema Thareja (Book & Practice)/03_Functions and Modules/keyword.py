def display(str,float_y,int_x):
    print("The string is: ",str)
    print("The float is: ",float_y)
    print("The integer is: ",int_x)

display(float_y = 0.876,int_x = 56, str = "Nishant") # Here order of arguments does not match with the parameter but using keywords can make it right

def display1(name,age,salary):
    print("Name: ",name)
    print("Age: ",age)
    print("Salary: ",salary)
display1(salary = 1900000,age = 25,name = "Nishant")
