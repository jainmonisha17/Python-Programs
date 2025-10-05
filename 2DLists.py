'''
[
    1 2 3
    4 5 6
    7 8 9
]

Its basically a list of list and it looks like this
matrix = 
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[2][2] = 9999
print(matrix[2][1])
print(matrix)

for row in matrix:
    for item in row:
        print(item)