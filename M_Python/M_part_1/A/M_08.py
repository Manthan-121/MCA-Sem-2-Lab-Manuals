def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

user_number = input("Enter a number: ")

if is_palindrome(user_number):
    print(user_number, "is a palindrome.")
else:
    print(user_number, "is not a palindrome.")
