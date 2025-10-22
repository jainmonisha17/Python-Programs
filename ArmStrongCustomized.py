def countDigits(number):
    count = 0

    while number > 0:
        number = number // 10
        count = count + 1
    return count

number = int(input("Enter a number: "))

original = number

power = countDigits(number)

armStrongNumSum = 0

def isArmStrong(number):
    while number > 0:
        base = number % 10
        armStrongNumSum = armStrongNumSum + (base ** power)
        number = number // 10

    return original == armStrongNumSum

flag = isArmStrong
if flag:
    print("Arm Strong number")
else:
    print("Not an Arm Strong number ")


