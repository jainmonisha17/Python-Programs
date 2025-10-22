def leapYear(year):
    if ((year % 100 != 0) and (year % 4 == 0)) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))

result = leapYear(year)
if result:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")
