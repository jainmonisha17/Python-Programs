class Parent:
    def __init__(self):
        self.a = 10
    
class child(Parent):
    def __init__(self):
        self.b = 20

c1 = child()
print(c1.b)
print(c1.a)