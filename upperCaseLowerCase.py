print("Enter any String: ")
string1 = input()
i = 0
newString = " "

while(i <= len(string1) - 1):
    extractedString = string1[i]
    asciiOfextractedString = ord(extractedString)

    if(asciiOfextractedString >= 65 and asciiOfextractedString <= 90):
        newAscii = asciiOfextractedString + 32
        convertedChar = chr(newAscii)
        newString = newString + convertedChar
    else:
        newString = newString + extractedString
    
    i = i + 1
print(newString)

    
