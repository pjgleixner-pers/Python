house = "Targaryen"

match house:
    case "Targaryen":
        print("House Targaryen: Fire and Blood")
    case "Stark":
        print("House Stark: Winter is Coming")
    case "Lannister":
        print("House Lannister: Hear Me Roar!")
    case _:
        print("Unknown House")