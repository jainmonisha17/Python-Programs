
    
List = []
i = 0
while(i <= 4):
    print("Enter the value: ")
    data = int(input())
    List.insert(i, data)
    i = i + 1
print(List) # [10, 11, 12, 13, 14]

k = list(filter(lambda num: (num % 2 == 0), List))
print(k) # [10, 12, 14]