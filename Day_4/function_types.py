#Function with argument and return type
def argfun(num1,num2):
    return num1+num2

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
print(f"Addition through function is: {argfun(num1,num2)}")