var1 = "Good"
print("The first outer variable is: ",var1)
def show():
    global var1 
    var1 = "Morning"
    print("The inner variable is: ",var1)
show()

var1 = "Fantastic"
print("The second outer variable is: ",var1)