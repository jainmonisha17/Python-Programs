class Hero:
    def __init__(self):
        self.name = "DBoss"
        self.age = 47
        self.mob = 98765
        self.noOfMovies = 55

    def act(self):
            print("Hero is acting")

    def dance(self):
            print("Hero is dancing")

h1 = Hero()
print(h1.name)
print(h1.age)
print(h1.mob)
print(h1.noOfMovies)

h1.noOfHits = 25
h1.address = "RR Nagar"

h1.mob = 667788
h1.age = 48

h2 = h1
h3 = h2
print(h3.name)
print(h3.age)
print(h1.mob)
print(h2.noOfMovies)
print(h3.noOfHits)
print(h2.address)

h3.act()
h2.dance()