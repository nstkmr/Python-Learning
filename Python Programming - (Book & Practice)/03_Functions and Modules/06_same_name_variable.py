def func():
    global str
    print(str) # Because str is now global it'll store the outer first
    str = "Hello world!!"
    print (str) # Now it'll change with the inner value
str = "Nishant Kumar"
func()
