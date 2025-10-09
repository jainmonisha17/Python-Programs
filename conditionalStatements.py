n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number2: "))
n3 = int(input("Enter a number3: "))

if n1 >= n2 and n1 >= n3:
    print(f"{n1} is the largest")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} is the largest")
else:
    print(f"{n3} is the largest")

print("End of the program")
