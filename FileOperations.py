import os

with open("example.txt", "w") as file:
    file.write("Hello, World!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    
file_to_delete = "example.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"{file_to_delete} has been deleted.")

