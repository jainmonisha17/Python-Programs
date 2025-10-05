def function1():
    a = 100
    b = 200
    c = a + b
    print("Funciton1: ", c)


def function2(x, y):
    x = 100
    y = 200
    c = x + y
    print("Function2: ", c)

def function3(x, y):
    c = x + y
    print("Function3: ", c)

def function4(x, y):
    c = x + y
    return c

function1()
print("-----------------------------")
result1 = function2()
print(result1)
print("-----------------------------")
a = 11
b = 22
function3(a, b)
result2 = function4(40, 50)
print("Function4: ", result2)


