class Student:
    def __init__(self):
        self.__name1 = " "
        self.__name2 = " "

    def getter1(self):
        return self.__name1

    def setter1(self, value):
        self.__name1 = value
    
    setGet = property(getter1, setter1)

    def getter2(self):
        return self.__name2
    def setter2(self, value):
        self.__name2 = value

    getSet = property(getter2, setter2)

s1 = Student()
s1.setGet = "Rama"
result1 = s1.setGet
print(result1)
s1.getSet = "Sita"
print(s1.getSet)