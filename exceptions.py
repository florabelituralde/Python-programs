import sys

x = int(input("value of x: "))
y = int(input("value of y: "))

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} divided by {y} is {result}")