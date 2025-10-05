def function1():
    print("Invoking Function1")

def function2(a, b):
    c = a + b
    print(c)

function1()
function2(11, 22)

# funciton1 without braces will print the address of function1
print(function1) # 5000
# funciton2 without braces will print the address of function2
print(function2)

print("---------------------------------")

ptr1 = function1 # <function function1 at 0x000002A4661C8B80>
ptr2 = function2 # <function function2 at 0x000002626E869800>

print("---------------------------------")

ptr1() # Invoking Function1
ptr2(10,20) # 30

print("---------------------------------")

print(ptr1) # <function function1 at 0x00000191BFEA8B80>
print(ptr2) # <function function2 at 0x000001B404A89800>