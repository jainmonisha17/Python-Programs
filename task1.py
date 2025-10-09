num = int(input("Enter a number: "))

if num > 0 and num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz Num")
elif num > 0 and num % 3 == 0:
    print("Fizz Num")
elif num > 0 and num % 5 == 0:
    print("Buss Num")
elif num <= 0:
    print("Neutral")
else:
    print("You have entered a number")
