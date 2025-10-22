def checkEvenOdd(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter number:  "))
flag = checkEvenOdd(number)
if flag:
    print(f"{number} is even")
else: 
    print(number, " is odd")
]79