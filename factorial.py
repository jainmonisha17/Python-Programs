number = int(input("Enter any number to find the factorial: "))
print(f"The factors of {number} are")

if number > 0:
    for seriesOfVal in range(1, number + 1):
        if number % seriesOfVal == 0:
            print(seriesOfVal, end=" ")

