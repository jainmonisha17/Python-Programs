def reverse_number(number):
    original = number
    reverse = 0

    if number < 0:
        number = number * (-1)
        while number > 0:
            digit = number % 10             # Extract last digit
            reverse = reverse * 10 + digit  # Append digit to reverse
            number = number // 10             # Remove last digit

        if original < 0:
            reverse = -reverse

    return reverse


num = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(num))
