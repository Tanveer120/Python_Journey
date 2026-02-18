num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"Both the numbers are equal")