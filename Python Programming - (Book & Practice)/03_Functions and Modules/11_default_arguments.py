def display(name,course = "MSc"): # Here we've set one parameter as default
    print("Name: "+ name)
    print("Course: ",course)

display(course = "BCA",name = "Nikhil") # Here it'll overwrite the default value
display(name = "Nishant") # Here we've called the function with one argument only

#def display1(name,course = "BTech",marks)    # This will throw an error b/c non-default argument follows default argument, it should be at last.