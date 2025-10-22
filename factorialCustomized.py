def factorial(number):
        for seriesOfValue in range(1, (number + 1)):
            if number % seriesOfValue == 0:
                print(number, end = " ")

number = int(input("Enter a number to find a factorial: "))

print(f"The factors of {number} are: ")
factorial(number)
