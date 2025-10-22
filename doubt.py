class Student:

    __name = "Rama"


    def __init__(self):
        self.__age = 50

    @property
    def accessingData(self):
        return self.__name

    @accessingData.setter
    def accessingData(self, value):
        self.__name = value
        self.__calling_setter()
        __a=10
        __b=20
        __c=__a+__b
        print(__c)
    
    def __calling_setter(self):
        print("This method is called during setter")

s1 = Student()
s1.accessingData = "Monisha" 
result1 = s1.accessingData
print(result1) 
#print(s1._Student.__name)