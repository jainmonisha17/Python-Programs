def function1():
    a = 10 # Non local variable
    print(a)

    def function2():
        a = 999
        b = 20  # Local variable 
        print("From function2, b:", b) # accessing local variable inside the nested function
        print("From function2, a:", a) # accessing non-local varialbe indside the nested function

    function2() 
    print("From function1, a:", a) 
    # print("From function1, b: ", b) # b is not defined here because it is a local variable to function2
function1()
# b is not defined here because it is a local variable to function2