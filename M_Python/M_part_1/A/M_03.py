def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

decimal_number = int(input("Enter a decimal number: "))

binary = decimal_to_binary(decimal_number)
octal = decimal_to_octal(decimal_number)
hexadecimal = decimal_to_hexadecimal(decimal_number)

print("Decimal:", decimal_number)
print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)
