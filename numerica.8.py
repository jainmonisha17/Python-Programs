start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

if start > end:
    print("Invalid input")
else:
    print("Even numbers")
    print("\t", end="")   # tab space

    for i in range(start, end + 1):
        if i % 2 == 0:        # even
            print(i, end=" ")

    print()  # move to next line

    print("Odd numbers")
    print("\t", end="")

    for i in range(start, end + 1):
        if i % 2 != 0:        # odd
            print(i, end=" ")
