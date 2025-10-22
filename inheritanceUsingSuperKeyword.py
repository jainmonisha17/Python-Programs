class A:
    def __init__(self):
        self.a = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 20

class C(B):
    def __init__(self):
        super().__init__()
        self.c = 30

objectCreation = C()

print(objectCreation.a)
print(objectCreation.b)
print(objectCreation.c)
