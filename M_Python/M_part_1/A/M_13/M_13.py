# Writing to a file
with open("demo.txt", "w") as file:
    file.write("Hello\n")
    file.write("World\n")
    file.write("Python\n")
    file.write("Programming\n")

# Reading from a file using readline()
print("Reading from file using readline():")
with open("demo.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())  # strip() to remove newline character
        line = file.readline()
print()

# Reading from a file using readlines()
print("Reading from file using readlines():")
with open("demo.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() to remove newline character
print()

# Writing lines to a file using write()
with open("demo.txt", "a") as file:
    file.write("This is a new line written using write()\n")

# Reading from a file after appending
print("Reading from file after appending:")
with open("demo.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() to remove newline character
print()

# Writing lines to a file using writelines()
with open("demo.txt", "a") as file:
    lines_to_write = ["Another line\n", "Yet another line\n", "One more line\n"]
    file.writelines(lines_to_write)

# Reading from a file after writelines()
print("Reading from file after writelines():")
with open("demo.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() to remove newline character
