def checkEvenOdd(number):
    return number % 2 == 0

number = int(input("Enter a number: "))
flag = checkEvenOdd(number)
if flag:
    print(f"{number} is even")
else:
    print(f"{number} is odd" )