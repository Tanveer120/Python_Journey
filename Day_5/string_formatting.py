num = 10000000

print(f"String in thousands using ,.0f : {format(num,',.0f')}")

print(f"Changing number of digits after decimal .2f : {format(num,'.2f')}")

print(f"Centering the String : {format(num,'^20')}")

print(f"Left align the String : {format(num,'<20')}")

print(f"Right align the String : {format(num,'>20')}")

print(f"Centering align with - both side the String : {format(num,'-^20')}")

print(f"Left align with - after the String : {format(num,'-<20')}")

print(f"Right align with - before the String : {format(num,'->20')}")