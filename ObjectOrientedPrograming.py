class Force_User:
    def __init__(self, name: str, lightsaber_color: str, forcepower: int):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.forcepower = forcepower
        
    def use_force(self):
        print(f"{self.name} uses the Force with power {self.forcepower}!")
        self.forcepower -= 10
            
luke = Force_User("Luke Skywalker", "Green", 100)
print(f"{luke.name} has a {luke.lightsaber_color} lightsaber. Force power: {luke.forcepower}")

luke.use_force()
print(f"{luke.name}'s remaining force power: {luke.forcepower}")

darth_vader = Force_User("Darth Vader", "Red", 120)

print(f"{darth_vader.name} has a {darth_vader.lightsaber_color} lightsaber. Force power: {darth_vader.forcepower}")

darth_vader.use_force()
print(f"{darth_vader.name}'s remaining force power: {darth_vader.forcepower}")
