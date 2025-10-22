# Program to print first N user defined even and odd numbers till the given range

def checkEven(number):
    return number % 2 == 0

countEven = int(input("Enter how many even natural numbers you want: "))
countOdd = int(input("Enter how many odd natural numbers you want: "))

series = 1
print("First 'N' even natural numbers are:")
while countEven > 0:
    if checkEven(series):
        print(series, end=" ")
        countEven = countEven - 1
    series = series + 1

series = 1
print("\nFirst 'N' odd natural numbers are:")
while countOdd > 0:
    if not checkEven(series):
        print(series, end=" ")
        countOdd = countOdd - 1
    series = series + 1
