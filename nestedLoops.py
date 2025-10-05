for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# range 5 -> 0 to 5(5 excluded)
# range 3 -> 0 to 3(3 excluded)
'''
x -> 0, y-> 0, 1, 2 -> (0, 0), (0, 1), (0, 2)
x -> 1, y-> 0, 1, 2 -> (1, 0), (1, 1), (1, 2)
x -> 2, y-> 0, 1, 2 -> (2, 0), (2, 1), (2, 2)
x -> 3, y-> 0, 1, 2 -> (3, 0), (3, 1), (3, 2)
x -> 4, y-> 0, 1, 2 -> (4, 0), (4, 1), (4, 2)
x -> 5, y-> 0, 1, 2 -> (5, 0), (5, 1), (5, 2)

'''

# outer loop for 2 lines printing 'x'
for numberOfLines in range(4):
    if numberOfLines % 2 == 0:
        #print xxxxx in even iterations
        for x in range(5):
            print('x', end='')
    else:
        for x in range(2):
            print('x', end='')
    print()  # Move to the next line
print('ENNNNNNNNNNNNNNNNNNNNNNDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
## Another exaample using range function and nested loops drawing 'F' shape using 'x's in python
'''
xxxxx
xx
xxxxx
xx
xx

'''


for numOfLines in range(4):
    if numOfLines % 2 == 0:
        #print xxxxx in even iterations
        for x in range(5):
            print('x', end='')
    else:
        for x in range(2):
            print('x', end='')
    print()


print('------------------------------------------------------------------------------------------------')
print()
print()
print()

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    print('x' * x_count)

print('------------------------------------------------------------------------------------------------')
print()
print()
print()

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for count in range (x_count):
        output += 'x'
    print(output)


print('------------------------------------------------------------------------------------------------')
print()
print()
print()

numbers = [9, 2, 9, 2, 2]

for x_count in numbers:
    output = ''
    for count in range (x_count):
        output += 'x'
    print(output)