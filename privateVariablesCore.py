class Book:
    def __init__(self):
        self.__pages = 100 # declaring private variable using double underscores __
    
    def setter(self, value):
        if(value > 0):
            self.__pages = value
    def getter(self):
        return self.__pages
b1 = Book()
b1.setter(114)
result = b1.getter()
print(result) 
b1.setter(-99)
print(b1.getter())