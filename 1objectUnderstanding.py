class Hero:
    def __init__(self):
        self.name = "Dboss"
        self.age = 30
        self.mobileNum = "99998888999"
        self.noOfMovies = 55

    def act(self):
        print(f"{self.name} is acting") 
        print(f"{self.name} is dancing")

    def dance(self):
        print("Hero is dancing")

h1 = Hero()
h1.act()
print(h1.name)
print(h1.age)
print(h1.mobileNum)
print(h1.noOfMovies)

