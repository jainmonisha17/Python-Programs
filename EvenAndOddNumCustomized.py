#  Write a program to print all the even and odd numbers available in a user defined range 

# Enter start range: 6
# End end range: 11

# Expected output: 

# Even numbers
#      6, 8, 10
# Odd numbers
#      7, 9, 11
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

if start > end:
    print("Invalid input")
else:
    print("Even numbers")
    print("\t", end = " ")
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end = " ")
    print()  # Move to the next line

    print("Odd numbers: ")
    print("\t", end = " ")
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number, end = " ")
    print()
