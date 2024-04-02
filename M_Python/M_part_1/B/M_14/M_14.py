import csv

def read_employee_data(file_name):
    employee_data = {}
    with open(file_name, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            emp_no = row['EmployeeNo']
            employee_data[emp_no] = row
    return employee_data

def print_salary_slip(emp_no, employee_data):
    if emp_no in employee_data:
        emp_details = employee_data[emp_no]
        print("Salary Slip for Employee Number:", emp_no)
        print("Name:", emp_details['amploy'])
        print("Department Number:", emp_details['DeptNo'])
        print("Basic Salary:", emp_details['Basic'])
        print("Dearness Allowance (DA):", emp_details['DA'])
        print("House Rent Allowance (HRA):", emp_details['HRA'])
        print("Conveyance:", emp_details['Conveyance'])
        total_salary = sum(float(emp_details[field]) for field in ['Basic', 'DA', 'HRA', 'Conveyance'])
        print("Total Salary:", total_salary)
    else:
        print("Employee with Employee Number", emp_no, "not found.")

def print_employee_list(dept_no, employee_data):
    print("Employee List for Department Number:", dept_no)
    for emp_no, details in employee_data.items():
        if details['DeptNo'] == dept_no:
            print("Employee Number:", emp_no)
            print("Name:", details['amploy'])
            print("Basic Salary:", details['Basic'])
            print()

# Read employee data from file
employee_data = read_employee_data("empData.csv")

# Test cases
print_salary_slip("1001", employee_data)
print()
print_employee_list("100", employee_data)
