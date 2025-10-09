def operation(data):
    return data + 10

Listt = []
i = 0

while(i <= 4):
    print("Enter the value: ")
    num = int(input())
    Listt.insert(i, num)
    i = i + 1

print(Listt)

k = list(map(operation, Listt))
print(k)