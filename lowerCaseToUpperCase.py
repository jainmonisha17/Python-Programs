print("Enter any string in lower cases: ")
string2 = input()
i = 0
newString = " "

while(i <= len(string2) - 1):
    extractedString = string2[i]
    ascii = ord(extractedString)

    if(ascii >= 97 and ascii <= 122):
        newAscii = ascii - 32
        convertedChar = chr(newAscii)
        newString = newString + convertedChar
    else:
        newString = newString + extractedString
    i = i + 1
print(newString)