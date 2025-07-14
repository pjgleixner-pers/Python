def greet_user(name):
    print(f"Hello, {name}!")

greet_user(input("Enter your name: "))

def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width

print(calculate_area_rectangle(float(input("Enter length: ")), float(input("Enter width: "))))
