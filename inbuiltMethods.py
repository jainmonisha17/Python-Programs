print("Enter the String: ")
string1 = input()
if(string1.isalpha()):
    print("String contais only characters")
elif(string1.isdigit()):
    print("String contains only numbers")
elif(string1.isalnum()):
    print("String contains both characters and numbers")
else:
    print("Enter a valid string")