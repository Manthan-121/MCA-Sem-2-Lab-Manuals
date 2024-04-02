def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

user_number = int(input("Enter a number: "))

if is_armstrong(user_number):
    print(user_number, "is an Armstrong number.")
else:
    print(user_number, "is not an Armstrong number.")
