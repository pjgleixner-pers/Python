try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError as e:
    print("thats not a valid number")
except ZeroDivisionError:
    print("Division by zero is not allowed")