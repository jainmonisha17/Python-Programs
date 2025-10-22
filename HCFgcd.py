number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

hcf = 1  # initialize with 1
lower = number1
if number2 < number1:
    lower = number2


for i in range(2, (lower) + 1):
    if(number1 % i == 0) and (number2 % i == 0):
        hcf = i  # updating hcf if i divides both numbers

print(hcf)