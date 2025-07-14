pokemon_caught = input("Enter the number of Pokémon caught: ")
pokemon_caught = int(pokemon_caught)

if pokemon_caught == 908:
    print("All Pokémon have been caught!")
else:
    print("keep catching Pokémon!")
    
#or

pokemon_caught = int(input("Enter the number of Pokémon caught: "))
if pokemon_caught != 908:
    print("keep catching Pokémon!")
else:
    print("All Pokémon have been caught!")
    
    
pokemonID = int(input("Enter the Pokémon ID: "))
if 0<= pokemonID <= 151 :
    print("You are in the Kanto region!")
elif 152 <= pokemonID <= 251:
    print("You are in the Johto region!")
elif 252 <= pokemonID <= 386:
    print("You are in the Hoenn region!")
elif 387 <= pokemonID <= 493:
    print("You are in the Sinnoh region!")
elif 494 <= pokemonID <= 649:
    print("You are in the Unova region!")
elif 650 <= pokemonID <= 721:
    print("You are in the Kalos region!")
elif 722 <= pokemonID <= 809:
    print("You are in the Alola region!")
elif 810 <= pokemonID <= 898:
    print("You are in the Galar region!")
else:
    print("This Pokémon ID is not recognized or is from a future generation.")
    