def isLeapYear(year):
    return ((year % 100 != 0) and (year % 4 == 0)) or (year % 400 == 0)

start = int(input("Enter starting year: "))
end = int(input("Enter ending year: "))

print("Leap Years:")
for year in range(start, end + 1):
    if isLeapYear(year):
        print(year)

print("Non-Leap Years:")
for year in range(start, end + 1):
    if not isLeapYear(year):
        print(year)
