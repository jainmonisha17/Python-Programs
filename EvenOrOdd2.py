start = int(input("Enter a start range: "))
end = int(input("Enter an end range: "))

if start > end:
    print("Invalid input!!")
else:
    print("Even numbers are: ")
    print("\t")
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end = " ")
    print()

    print("Odd numbers: ")
    print("\t")
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number, end = " ")
    print()