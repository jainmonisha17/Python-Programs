class Student:
    def __init__(self, name, age, address, height):
        self.name = name
        self.age = age
        self.address = address
        self.height = height

S1 = Student("Rama", 22, "Hydrabad", 5.6)
S2 = Student("Sita", 20, "Banglore", 5.4)

print(S1.name)
print(S2.name)