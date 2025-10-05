a = 999

def function1():
    a = 888
    b = 777
    print(a)
    print(b)

def function2():
    a = 666
    c = 555
    print(a)
    print(c)

print("Printing a Global variable a = 999 which is called outside the function")
print(a)

print("------------------------")

print("Printing a local variable a = 888 and b = 777 which is called inside the function")

function1()

print("------------------------")

print("Printing a local variable a = 666 and c = 555 which is called inside the function")

function2()

print("------------------------")

print("Printing a Global variable a = 999 which is called outside the function")
print(a)
