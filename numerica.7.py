# Function to check even or odd
def checkEvenOdd(number):
    return number % 2 == 0

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

if start > end:
    print("Invalid input")
else:
    print("Even numbers")
    print("\t", end="")  # tab space

    for i in range(start, end + 1):
        if checkEvenOdd(i):    # if even
            # Print with comma, but no extra comma at the end
            if i + 2 <= end or (i + 2 > end and checkEvenOdd(i + 2)):
                print(i, end=", ")
            else:
                print(i, end="")
    print()  # new line

    print("Odd numbers")
    print("\t", end="")  # tab space

    for i in range(start, end + 1):
        if not checkEvenOdd(i):    # if odd
            if i + 2 <= end or (i + 2 > end and not checkEvenOdd(i + 2)):
                print(i, end=", ")
            else:
                print(i, end="")
