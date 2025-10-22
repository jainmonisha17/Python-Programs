number = int(input("Enter a number: "))
original = number
reverse = 0

temp = abs(number)

while temp > 0:
    digit = temp % 10       # get last digit
    reverse = reverse * 10 + digit   # append digit to reverse
    temp = temp // 10       # remove last digit

# If original number was negative, make reverse negative
if original < 0:
    reverse = -reverse

print("Reversed number:", reverse)
