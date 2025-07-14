class Force_User:
    def __init__(self, name: str, lightsaber_color: str, forcepower: int):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.forcepower = forcepower
        
    def use_force(self):
        print(f"{self.name} uses the Force with power {self.forcepower}!")
        self.forcepower -= 10
        print(f"{self.name}'s remaining force power: {self.forcepower}")
            
luke = Force_User("Luke Skywalker", "Green", 100)
print(f"{luke.name} has a {luke.lightsaber_color} lightsaber.")
luke.use_force()

darth_vader = Force_User("Darth Vader", "Red", 120)
print(f"{darth_vader.name} has a {darth_vader.lightsaber_color} lightsaber.")
darth_vader.use_force()