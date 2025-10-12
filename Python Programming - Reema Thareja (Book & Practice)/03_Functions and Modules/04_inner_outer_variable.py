def outer_func():
    var1 = "10"
    def inner_func():
        var2 = "20"
        print("The outer variable is: ",var1)
        print("The inner variable is: ",var2) # It can access both outer and inner variables

    inner_func() # Calling the defined inner function 
    print("The outer variable is: ",var1)
    print("The inner variable is: ",var2) # Outer function can't access the inner function's variable. It'll throw an error

outer_func() # Calling the defined outer function