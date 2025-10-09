num = int(input("Enter a number: "))

if num <= 0:
    print("Neutral")
elif num > 0 and num % 3 == 0:
    print("Fizz Num")
elif num > 0 and num % 5 == 0:
    print("Buzz Num")
elif num > 0 and num % 3 and num % 5 == 0:
    print("Fizz Buzz Num")
else:
    print("You have entered a number")
