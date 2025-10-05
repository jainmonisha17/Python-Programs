names = ['Monisha', 'Ullas', 'Bea', 'Dia', 'Sameer']
print(names)
print(names[3])
print(names[-1])  # negative index -1 gives last index element, -2 gives last but one indexed element, -3 gives last but second indexed element and so on
print(names[-3])  # last indexes means negative indexes starts from -1(means from negative first eleemnt not from negative 0th indexed element)
print(names[-5])

print('________________________________________________________________')
print()
print()
print()
print(names[2:]) # 2nd index to last index
print(names[2:4]) # 2nd index to 3rd index (2:4) -> 4 is excluded
print(names[1:5]) # 1 to 4
print(names[-5: -1]) # 5 to 1 but 1 is not included
print(names[:]) # to print all

# the original list is not affected it just creates the copy of the original list 
print("The original list is displaying here:")
print(names)
# to update the list
names[1] = "Ullas JAIN"
print(names)

print(names)
# Here original list can be updated and it displayes only the original list to us after updating or making changes


print()
print()
print()

# Now find the largest number in the list
numbers = [3, 6, 2, 8, 4, 10, 12]
max = numbers[0] # here we are intially assuming that the first number itself is the larget number, chances are our assumptions could be wrong

for largestNumber in numbers:
    if largestNumber > max:
        max = largestNumber
print(max)
