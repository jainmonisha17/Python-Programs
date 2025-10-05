customer = {
    "name": "Monisha Jain",
    "age": 24, 
    "is_verified": True
}
print(customer["name"])
# Dictionaries are case sensitive and can't be repeated
print(customer.get("birthDate", "Dec 17 2000"))
customer["name"] = "Bea Jain"
print(customer["name"])


phone = input("Phone:")

number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10

}

for ch in phone:
    output = output + number.get(ch, "!")
print(output)