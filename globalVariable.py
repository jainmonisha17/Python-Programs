a = 10
def function1():
    print(a)
    b = 20
    print(b)

def function2():
    print(a)
    c = 30
    print(c)

print("Printing a global variable: ")
print(a)

print("------------------------")

print("Calling a function1: ")
function1()

print("------------------------")

print("Calling a function2")
function2()

print("------------------------")

print("Again printing a global variable")
print(a)
