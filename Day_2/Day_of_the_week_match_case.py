num1 = int(input("Enter the day number where 1 = Sunday: "))
a=True

while a == True:
    if num1 > 7:
        num1 -= 7
    else:
        a = False

match num1:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")