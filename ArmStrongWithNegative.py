def countDigits(number):
    count = 0
    temp = number
    if temp < 0:
        temp = -temp  
    while temp > 0:
        temp = temp // 10
        count += 1
    return count

def isArmStrong(original):
    temp = original
    if temp < 0:
        temp = -temp  
    
    power = countDigits(original)
    armStrongNumSum = 0
    
    while temp > 0:
        digit = temp % 10
        armStrongNumSum += digit ** power
        temp //= 10
    
    if original < 0: # if the input was negatie then covert the sum to negative
        armStrongNumSum = -armStrongNumSum
    
    return original == armStrongNumSum


number = int(input("Enter a number: "))

flag = isArmStrong(number) 
if flag:
    print("Arm Strong number")
else:
    print("Not an Arm Strong number")
