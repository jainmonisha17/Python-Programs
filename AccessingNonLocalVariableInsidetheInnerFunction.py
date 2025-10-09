def function1():
    a = 100
    print("From function1, a:", a)

    def function2():
        nonlocal a # to access the non-local variable 'a' from function1
        a = 999 # this will update the value of 'a' in function1
        b = 200 # Local variable
        print("From function2, b:", b) # accessing local varialbe inside the nested function
        print("From function2, a:", a) # accessing non-local variable inside the nested function

    function2() # calling the nested function
    print("From function1, a:", a) # accessing non-local variable inside the function1lo
    # print("From funciton1, b:", b) # b is not defined here because it is a local variable to function2
function1() # b is not defined here also
