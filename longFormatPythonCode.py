class Demo:
    def add(self, a, b):
        result1 = a + b
        return result1
    
    def subtract(self, a, b):
        result2 = a - b
        return result2
    
    def multiply(self, a, b):
        result3 = a * b
        return result3
    
    def divide(self, a, b):
        result4 = a / b
        return result4
    
d = Demo()
a = 20
b = 10
x1 = d.add(a, b)
print("Addition: ", x1)

x2 = d.subtract(a, b)
print("Subtraction: ", x2)

x3 = d.multiply(a, b)
print("Multiplication: ", x3)

x4 = d.divide(a, b)
print("Division: ", x4)
    
