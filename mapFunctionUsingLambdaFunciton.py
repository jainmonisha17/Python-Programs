myList = []
i = 0

while(i <= 4):
    print("Enter the value: ")
    num = int(input())
    myList.insert(i, num)
    i = i + 1

print(myList) # [10, 11, 12, 13, 14]

k = list(map(lambda data: data + 10, myList))
print(k) # [20, 21, 22, 23, 24]