while True:
    number = int(input("Enter a number: "))
    if number == 8:
        break
    elif number % 3 == 0 and number %5 == 0:
        continue
    print("The number is: ", number)
print()