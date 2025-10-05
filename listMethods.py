numbers = [5, 2, 4, 4, 4, 7, 9]
numbers.append(888)
print(numbers)

# but what if you want to add any number in the middle of the list?
numbers.insert(0, 33)
print(numbers)

print()
# to remove any number
print("# to remove any number")
numbers.remove(2)
print(numbers)

print()

# to remove all the numbers
print("# to remove all the numbers")
numbers.index(33)
print(numbers.index(5))

print()

# to remove the last item in that list
print("# to remove the last item in that list")
numbers.pop()
print(numbers)

print()

# to check the existence of any number in the list. (Returns True or False)
print("# to check the existence of any number in the list. (Returns True or False)")
print(50 in numbers)

print()

# to count the number repeated 
print("# to count the number repeated ")
print(numbers.count(4))
print()

# to sort the numbers in-place that we are not able to see it but in-place it is sorted
print("# to sort the numbers in-place that we are not able to see it but in-place it is sorted")
print(numbers.sort()) # in-place it is sorted

print()

# to sort all the numbers in a ascending order by defalut
print("# to sort all the numbers in a ascending order by defalut")
numbers.sort()
print(numbers)

print()

# to reverse the list
print("# to reverse the list")
numbers.reverse()
print(numbers)

print()

numbersCopy = numbers.copy()
numbers.append(10090)
print("Original list of numbers")
print(numbersCopy)
print("Copied list of numbers")
print(numbers)

print()

# to remove the duplicates in the list
print("# to remove the duplicates in the list")
numbersDuplicated = [2, 2, 4, 4, 4, 3, 3, 2, 5, 6, 7, 7, 8, 8, 9, 8, 9]
uniques = []

print()
for number in numbersDuplicated:
    if number not in uniques:
        uniques.append(number)

print(uniques)