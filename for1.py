class Demo:
    def __init__(self):
        self.x = 100
        self.y = 200

    def add(self, a, b):
        c = a + b
        print(c)

d = Demo()
print(d.x)
print(d.y)

a = 40
b = 50
d.add(a, b)

