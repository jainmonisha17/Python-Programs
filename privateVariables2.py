class Person:
    def __init__(self):
        self.__name = " "

    def getter1(self):
        return self.__name
    def setter1(self, value):
        self.__name = value
p = Person()
p.setter1("Rama")
print(p.getter1())