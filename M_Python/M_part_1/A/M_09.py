user_string = input("Enter a string: ")

vowel_count = sum(1 for char in user_string if char.lower() in "aeiou")
print("Number of vowels:", vowel_count)

length = sum(1 for _ in user_string)
print("Length of string:", length)

reversed_str = user_string[::-1]
print("Reversed string:", reversed_str)

find_str = input("Enter the string to find: ")
replace_str = input("Enter the string to replace with: ")
replaced_str = user_string.replace(find_str, replace_str)
print("After find and replace operation:", replaced_str)

is_palindrome = user_string == user_string[::-1]
print("The string is a palindrome." if is_palindrome else "The string is not a palindrome.")