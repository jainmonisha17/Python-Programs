def checkEvenOdd(number):
    return number % 2 == 0

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

if start > end:
    print("Invalid input")
else:
    print("Even numbers: ", end="")

    for i in range(start, end + 1):
        if checkEvenOdd(i):
            print(i, end=" ")
