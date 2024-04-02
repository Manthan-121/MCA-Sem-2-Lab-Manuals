import csv

def process_csv(file_name):
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Process the CSV file
process_csv("empData.csv")
