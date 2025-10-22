def checkEvenOdd(number):
    return number % 2 == 0

coundEven = int(input("Enter how many even natural numbers you want: "))
countOdd = int(input("Enter how many odd natural numbers you want: "))

print("First even natural numbers are: ")
series = 1
while coundEven > 0:
    result = checkEvenOdd(series)
    if result:
        print(series, end = " ")
        coundEven = coundEven - 1
    series = series + 1

print("\n First odd natural numbers are: ")
series = 1
while countOdd > 0:
    result = checkEvenOdd(series)
    if not result:
        print(series, end = " ")
        countOdd = countOdd - 1
    series = series + 1
