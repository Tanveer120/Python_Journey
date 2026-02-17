# str = input("Enter the string: ")
# print("The string is: ", str)

# num1 = int(input("Enter the 1st Number: "))
# print("The 1st number is: ", num1)

day = int(input("Enter the day number: "))
month = int(input("Enter the Month: "))
year = int(input("Enter the Year: "))

#Formatted string output
print(f"{day}-{ "0" if month < 10 else ""}{month}-{year}")