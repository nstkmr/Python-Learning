def outer_func():
    var = "10"
    def inner_func():
        global var # We still can't access it from the outer function
        var = "20" # We can assign a new value to the same name variable in inner function
        print("The inner variable is: ",var) 

    print("The outer variable is: ",var) # As outer function can't access the inner variable, so the value won't change

    inner_func()

outer_func()
