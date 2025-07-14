fellowship = { 
              "Wizzard": "Gandalf",
              "Hobbit": "Frodo",
              "Elf": "Legolas"
              }

print(fellowship)
print(fellowship["Wizzard"])

#adding a new key-value pair
fellowship["Dwarf"] = "Gimli"
print(fellowship)

#updating an existing key-value pair
fellowship["Elf"] = "Legolas Greenleaf"
fellowship["Wizzard"] = "Gandalf the Grey"
print(fellowship)

#print keys, values, and items
print(fellowship.keys())
print(fellowship.values())
print(fellowship.items())