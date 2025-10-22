def checkEvenOdd(number):
    return number % 2 == 0

number = int(input("Enter a number of your choice: "))
result = checkEvenOdd(number)

if result:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")