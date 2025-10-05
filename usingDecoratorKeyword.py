class Demo:
    x = 11

    def __init__(self):
        self.y = 22
        self.z = 33

    def instance_method(self):
        print("Instance Method")
        print(self.x) # Accessing instance variable inside instance method using self
        print(self.y) # Accessing instance variable inside instance method using self

    @staticmethod
    def static_method():
        print("Static Method")
        print(Demo.x) # Accessing class variable inside static method using class name
        # print(self.y) # Error: Cannot access instance variable inside static method
        # print(self.z) # Error: Cannot access instance variable inside static method
        
        Demo.x = 1212 # Modifying class variable inside static method using class name
        print(Demo.x) # Accessing modified class variable inside static method using class name

    @classmethod
    def class_method(cls):
        print("Class Method")
        print(cls.x) # Accessing class variable inside class method using cls
        cls.x = 1312121 # Modifying class variable inside class method using cls
        print(cls.x) # Accessing modified class variable inside class method using cls

Demo.static_method()
print("------------------------------------------------------")
Demo.class_method()
d = Demo()
print("------------------------------------------------------")
d.instance_method()
print("------------------------------------------------------")
d.static_method()
print("------------------------------------------------------")
d.class_method()
print("------------------------------------------------------")

