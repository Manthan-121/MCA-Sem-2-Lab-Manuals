def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num_terms = int(input("Enter the number of terms: "))

print("Fibonacci series up to", num_terms, "terms:")
for i in range(num_terms):
    print(fibonacci(i))
