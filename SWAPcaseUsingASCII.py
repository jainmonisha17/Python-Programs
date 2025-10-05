print("Enter any string: ")
string = input()
i = 0
newString = " "

while(i <= len(string) - 1):
    extractedString = string[i]
    ascii = ord(extractedString)

    if(ascii >= 65 and ascii <= 90):  # uppercase + 32 = lowercase
        newAscii = ascii + 32
        convertedChar = chr(newAscii)
        newString = newString + convertedChar
    else:
        newAscii = ascii - 32
        convertedChar = chr(newAscii)
        newString = newString + convertedChar
    
    i = i + 1
print(newString)