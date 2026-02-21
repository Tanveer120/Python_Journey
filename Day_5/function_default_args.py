def print_name(name="MSQ"):
    name = name or "MSQ"
    print(f"The name is: {name}")

name = input("Enter the name: ")
print_name(name)
print_name()
