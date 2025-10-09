a = 10
print(a) # 10

b = (2  * 5)
print(b) # 10

c = (10 ** 1)
print(c)

print(a == b == c)
print(id(a) == id(b) == id(c)) # True

c = 15
print(id(c)) #140727761360104

c = 20
print(id(c)) # 140727761360264

c = 25
print(id(c)) # 140727761360424

# id's holds the updated value of c
# one variabe can hold different values at different times
# multiple value into the same variable it will always points to the latest updated value
# we think that we are changing the value of c but in reality we are creating a new object in the memory and c is pointing to the new object.

d = 1, 2, 3
print(d)
print(type(d)) # <class 'tuple'>
# A tuple is a collection data type in Python.
# It is similar to a list, but with one big difference:
# Tuples are immutable (once created, you cannot change, add, or remove elements).

 