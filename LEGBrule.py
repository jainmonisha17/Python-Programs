x = 10 # Global variable
def function1():
    # x = 12 # Non-local variable

    def function2():
        # x = 20 # local variable
        print(x)
    function2()
function1()