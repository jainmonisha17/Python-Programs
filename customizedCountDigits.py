def countDigit(number):
    count = 0

    while number > 0:
        number = number // 10
        count = count + 1
    return count
number = int(input("Enter the digits: "))
result = countDigit(number)
print(f"The count of digits in {number} is: {result}")