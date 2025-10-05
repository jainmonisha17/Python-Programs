class Heroine:
    def __init__(self):
        self.name = "Ramya"
        self.age = 35
        self.address = "Banglore"
        self.mobileNumber = 9876543210

    def act(self):
        self.height = 5.4

h = Heroine()
h.act()
h.name = "Radika"
h.color = "white"

print(h.name)
print(h.age)
print(h.address)
print(h.mobileNumber)
print(h.height)
print(h.color)
