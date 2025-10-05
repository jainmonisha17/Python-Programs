def even(num):
    if(num % 2 == 0):
        return True
    else:
        return False
    
List = []
i = 0
while(i <= 4):
    print("Enter the value: ")
    data = int(input())
    List.insert(i, data)
    i = i + 1
print("Original list containing even and odd numbers", List) # [10, 11, 12, 13, 14]

k = list(filter(even, List))
print("Even numbers in the given list are: ", k) # [10, 12, 14]

