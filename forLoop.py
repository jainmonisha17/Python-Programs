for item in 'Car Driving':
    print(item)

for names in ['Roopa', 'Ullas', 'Monisha', 'Mana', 'Bea', 'Pappa']:
    print(names)

# Range functions in a simple way if we want to type from 1 to 100 easily but not the last number is printed in range function
for item in range(1, 20, 2): # 1 to 20(exclucded with 2 steps forward)
    print(item)

for number in range(9, 49, 3):
    print(number) # 9 to 49(excluded) with 3 steps forward 

prices = [10, 20, 30, 40, 50]

total = 0
for price in prices:
    total = total + price
print(f"Total: {total}")