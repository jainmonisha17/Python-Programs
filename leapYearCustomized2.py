def isLeapYear(year):
    if ((year % 100 != 0) and (year % 4 == 0)) or (year % 400 == 0):
        return True
    else:
        return False

start = int(input("Enter starting year: "))
end = int(input("Enter ending year: "))

print(f"Leap years between {start} and {end} are:")

for year in range(start, end):
    if isLeapYear(year):
        print(year)
