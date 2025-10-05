class Demo:
    def swap(self, a, b):
        temp = a
        a = b
        b = temp
        print("a value: ", a)
        print("b value: ", b)

d = Demo()
x = 10
y = 20
print("Before Swapping")
print("x value: ", x)
print("y value: ", y)
print("After Swapping")

d.swap(x, y)


