num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

maximum = num1
if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3

minimum = num1
if num2 < minimum:
    minimum = num2
if num3 < minimum:
    minimum = num3

print("Maximum number:", maximum)
print("Minimum number:", minimum)
