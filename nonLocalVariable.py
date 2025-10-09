def function1():
    a = 10  # Non-local variable
    print("From function1, a:", a) # accessing non-local variable inside the function1

    def function2():
        b = 20 # local variable
        print("From function2, b:", b)
        print("From function2, a:", a) # accessing non-local variable inside the nested function

    function2()
    print("From function1, a:", a)
    # print("From function1, b: ", b)
function1() # b is not defined here because it is a local variable to funtion2
