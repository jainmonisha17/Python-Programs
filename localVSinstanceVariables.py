class Caluculator:
    def __init__(self):
        self.x = 100
        self.y = 200

    def add(self):
        a = 10
        b = 20
        c = a + b
        print("The sum is:", c)

    def sub(self):
        num1 = 40
        num2 = 20
        diff = num1 - num2
        print("The difference is:", diff)

c1 = Caluculator()
c1.add()
c1.sub()