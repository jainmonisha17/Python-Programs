def function1():
    print("Invoking function1")

def function2(a, b):
    c = a + b
    print("Sum is: ", c)

def display(ptr1, ptr2):
    ptr1()
    ptr2(30, 40)



function1()
a = 100
b = 200
function2(a, b)

ptr3 = function1
ptr4 = function2

ptr3()
ptr4(20, 30)

display(ptr3, ptr4)