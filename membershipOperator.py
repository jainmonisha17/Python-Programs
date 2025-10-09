myList = [1, 3, 8, -9]
print(myList[1]) # 3
print(myList[3]) # -9
print(3 in myList) # True
print([-9] in myList) # False


# a = (2 * 4)
# print(a not in myList) # True
# print(8 in a) # Error


print(8 in 88) # TypeError: argument of type 'int' is not iterable
print("8" in "88") #True
print(8 in "88") # False TypeError: arguement of type 'str' is not iterable
print("a" in "apple") #True
print(8 in 88) # TypeError: arguemnt of type 'int' is not iterable
print("a" in ["apple", "strawberry"]) # True

a = 5
b = (4 + 1)
c = (5 - 0)

print(a is id(5)) # True
print(id(5)) # id(5) returns a number representing the memory address of the integer 5
# It does not return the object itself, so this expression doesn’t do what you might think.
print(a is b is c) # Shaaring the memory having the same id
print(a is not 'b')
print(a is 5)