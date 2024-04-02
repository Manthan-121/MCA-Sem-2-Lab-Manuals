def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Taking user input
num = int(input("Enter a number for factorial : "))

# Calculating and printing factorial
print("Factorial of", num, " is :", factorial(num))
