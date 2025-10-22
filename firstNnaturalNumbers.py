# Write a progarm to print first 'N' even natural numbers:

def checkEvenOdd(number):
    return number % 2 == 0

count = int(input("Enter a last or till number till you want to see the first 'N' natural numbers: "))
series = 1

while count > 0:
    result = checkEvenOdd(series)

    if result:
        print(series, end = " ")
        count = count - 1
    series = series + 1


