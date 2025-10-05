'''
if name is less than 3 characters long
    name must be atleast 3 characters
otherwise if its more than 50 characters long
    name can be a maximum of 50 characters
otherwise
    name looks good!
'''

name = "MonishaaaaaaaaaaaaaaaaaaaaaaaaaaaljfkruilllULLASBEAROOPAjkkkkkkkkkkkkkkkkkkkkhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"

print(len(name))

if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name) > 50:
    print("Name can be maximum of 50 characrers")
else:
    print("Name looks good")

