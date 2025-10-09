myList = ["Rama", "Krishna", "Arjuna", "Bheema", "Radha", "Rukmini"]

filterNames = list(filter(lambda name: name.startswith("R"), myList))
print("Filtering names starting with R:", filterNames) # ["Rama", "Radha", "Rukmini"]

mapNames = list(map(lambda name: name.upper(), myList))
print("Using upper case for the whole list when we send the whole list: ", mapNames) # ["Rama", "Krishna", "Arjuna", "Bheema", "Radha", "Rukmini"]

mapNames = list(map(lambda name: name.upper(), filterNames))
print("Using upper case for the whole list when we send the filterNames list instead of whole list: ", mapNames) # ["Rama", "Krishna", "Arjuna", "Bheema", "Radha", "Rukmini"]

combined = list(map(lambda name: name.upper(), filter(lambda name: name.startswith("R"), myList)))
print(combined) # ["Rama", "Radha", "Rukmini"] 