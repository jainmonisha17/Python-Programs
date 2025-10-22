class Cargo:
    def takeOff(self):
        print("Plane is taking off")

    def fly(self):
        print("Plane is flying")

    def land(self):
        print("Plance is landing")
    
    def carry(slef):
        print("Plance is carrying cargo")

class Passenger:
    def takeOff(self):
        print("Plance is taking off")

    def fly(self):
        print("Plane is flying")

    def land(self):
        print("Plane is landing")

    def carry(self):
        print("Plane carry passengers")

class Fighter:
    def takeOff(slef):
        print("Plane is taking off")

    def fly(self):
        print("Plance is flying")

    def land(self):
        print("Plane is landing")
    
    def carry(self):
        print("Plane carry weapons")

c = Cargo()
p = Passenger()
f = Fighter() # f is holding the object address of Fighter class

c.takeOff()
c.fly()
c.land()
c.carry()

p.takeOff()
p.fly()
p.land()
p.carry()

f.takeOff()
f.fly()
f.land()
f.carry()

