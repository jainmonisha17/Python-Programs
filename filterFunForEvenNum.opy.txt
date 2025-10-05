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
print(List) # [10, 11, 12, 13, 14]

i = 0
while(i <= 4):
    extract = List[i]
    status = even(extract)
    if(status == True):
        print(List[i])
    i = i + 1