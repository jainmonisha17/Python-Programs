class Fan:
    def __init__(self):
        self.brand = "Bajaj"
        self.color = "Black"
        self.cost = 2500
        self.noOfBlades = 3

    def on(self):
            print("Fan is ON")
    def off(self):
            print("Fan is OFF")

f1 = Fan()
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.noOfBlades)

f1.on()
f1.off()   