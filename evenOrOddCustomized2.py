def checkEvenOdd(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
number = int(input("Enter a number to check if its even or odd: "))
result = checkEvenOdd(number)

if result:
    print(f"{number} is an even number!!")
else:
    print(f"{number} is an odd number")