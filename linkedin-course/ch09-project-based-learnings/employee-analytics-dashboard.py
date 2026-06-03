#   Generate total employees, department counts, average salary, highest paid employee, and employees joined this year.

# each employee is represented as a dictionary with keys: name, department, salary, and joined_year
from datetime import datetime
employee_1 = {"name": "John", "department": "sysadmin",
              "salary": 50000, "joined_year": 2020}
employee_2 = {"name": "Jane", "department": "HR",
              "salary": 60000, "joined_year": 2021}
employee_3 = {"name": "Doe", "department": "sysadmin",
              "salary": 55000, "joined_year": 2021}
employee_4 = {"name": "Smith", "department": "Finance",
              "salary": 70000, "joined_year": 2020}
employee_5 = {"name": "Emily", "department": "HR",
              "salary": 65000, "joined_year": 2022}
employee_6 = {"name": "Wilson", "department": "Engineering",
              "salary": 45000, "joined_year": 2019}
employee_7 = {"name": "Olivia", "department": "Engineering",
              "salary": 48000, "joined_year": 2022}
employee_8 = {"name": "Michael", "department": "Finance",
              "salary": 72000, "joined_year": 2021}
employee_9 = {"name": "Sophia", "department": "sysadmin",
              "salary": 53000, "joined_year": 2020}

# group of employees is represented as a list of dictionaries
company = [employee_1, employee_2, employee_3, employee_4,
           employee_5, employee_6, employee_7, employee_8, employee_9]


# total employees
total_employees = len(company)
# print(f"Total employees: {total_employees}")

# ------------------------------------------department counts-------------------------------

# 1st attempt
engineering_employees = []
sysadmin_employees = []
finance_employees = []
hr_employees = []
for employee in company:
    if (employee.get("department") == "sysadmin"):
        sysadmin_employees.append(employee)
    if (employee.get("department") == "Engineering"):
        engineering_employees.append(employee)
    if (employee.get("department") == "Finance"):
        finance_employees.append(employee)
    if (employee.get("department") == "HR"):
        hr_employees.append(employee)

department_counts = {"engineering": len(engineering_employees),
                     "sysadmin": len(sysadmin_employees), "Finance": len(finance_employees), "HR": len(hr_employees)}
# print(f"Department count: {department_counts}")

# optimized attempt
department_counts = {}

for employee in company:
    department = employee.get("department")
    department_counts[department] = department_counts.get(
        department, 0)+1

print(f"Department count: {department_counts}")

# ------------------------------------------average salary-------------------------------

# 1st attempt
total_salary = 0
for employee in company:
    total_salary += employee.get("salary")

average_salary = total_salary/total_employees
# print(f"Average Salary:{average_salary}")

# optimized attempt
total_salary = sum(employee.get("salary")for employee in company)
average_salary = total_salary/total_employees
print(f"Average Salary:{average_salary}")

# ------------------------------------------highest paid employee-------------------------------

# 1st attempt
max_salary = 0
for employee in company:
    max_salary = max(max_salary, employee.get("salary"))

for employee in company:
    if (employee.get("salary") == max_salary):
        max_salary_employee = employee
# print(f"Max Salary:{max_salary_employee}")

# 2nd attempt
highest_paid_employee = company[0]
max_salary = company[0]["salary"]

for employee in company:
    if (employee.get("salary") > max_salary):
        max_salary = employee.get("salary")
        highest_paid_employee = employee
# print(f"Max Salary:{highest_paid_employee}")

# optimized attempt - using lambda function
highest_paid_employee = max(company, key=lambda employee: employee["salary"])
print(f"Max Salary:{highest_paid_employee}")

# ------------------------------------------employees joined this year-------------------------------

# 1st attempt
employees_2022 = []
for employee in company:
    if (employee.get("joined_year") == 2022):
        employees_2022.append(employee)

# print(f"employees joined this year:{employees_2022}")

# optimized attempt - using datetime.now()
current_year = datetime.now().year
employees_this_year = []
for employee in company:
    if (employee.get("joined_year") == current_year):
        employees_this_year.append(employee)
print(f"employees joined this year:{employees_this_year}")
