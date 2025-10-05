weight = int(input("Weight:"))
unit = input('(L)bs or (K)g: ')


# note that weight that is inputed by the user is in "String" format and output should be int format sooo!! 
# we are getting input weight in string and then and there only we convert it into int and proceed with int
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
