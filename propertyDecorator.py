class Student:
    def __init__(self):
        self.__name = " "

    @property
    def accessingData(self):
        return self.__name

    @accessingData.setter
    def accessingData(self, value):
        self.__name = value

s1 = Student()
s1.accessingData = "Monisha"
result1 = s1.accessingData
print(result1) 