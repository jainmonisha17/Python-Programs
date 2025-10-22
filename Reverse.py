def reverse_number(num):
    original = num
    rev = 0

    if num < 0:
        num = -num   

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if original < 0:
        rev = -rev

    return rev


num = int(input("Enter a number: "))
reversed_num = reverse_number(num)

print("Reversed Number:", reversed_num)


# Palindrome check
if num == reversed_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
