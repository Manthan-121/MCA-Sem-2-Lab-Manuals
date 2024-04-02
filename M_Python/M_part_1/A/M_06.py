numbers = []
for i in range(10):
    number = float(input("Enter number {}: ".format(i + 1)))
    numbers.append(number)

largest_odd = None
for number in numbers:
    if number % 2 != 0: 
        if largest_odd is None or number > largest_odd:
            largest_odd = number

if largest_odd is not None:
    print("The largest odd number is:", largest_odd)
else:
    print("No odd numbers found.")
