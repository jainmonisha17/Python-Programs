def checkEvenOdd(number):
    return number % 2 == 0

count = int(input("Enter a number: "))
series = 1

while count > 0:
    result = checkEvenOdd(series)
    if result:
        print(series, end = " ")
        count = count - 1
    series = series + 1