

def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard!")

print("Start")
greet_user("Monisha")
greet_user("Bea")
greet_user("Ullas")
greet_user("Roopa")
greet_user("Suhu")

print("End")

# Parameters is a placeholder for the value we pass to th function
# Argumesnts are the actual values we pass to the function
'''
def greet_user(Paramter):
    print("")

print("Start")
greet_user("Argument")
print("End")
'''

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard!")

print("Start")
greet_user("Monisha", "Jain")
print("End")
