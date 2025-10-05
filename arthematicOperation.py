class Demo:
    def arthematic_Operation(self, a, b):
        add = a + b
        sub = a - b
        mul = a * b
        div = a / b

        return add, sub, mul, div

d = Demo()
a = 20
b = 10
x1, x2, x3, x4 = d.arthematic_Operation(a, b)
print()

# cursor will enter to return statement which is returning multiple values, cursor will out of the return statement, it is carrying 4 written values

print("Addition: ", x1)
print("Subtrction: ", x2)
print("Multiplication: ", x3)
print("Division: ", x4)

print(f"Addition: {x1}\nSubrction: {x2}\nMultiplication: {x3}\nDivision: {x4} \n")

print(f"{x1}\n{x2}\n{x3}\n{x4}\n")