#Define the Class 
class Employee:

    def __init__(self):
        self.employee_id = None
        self.name = None
        self.role = None
        self.salary = None

    def display_details(self):
        print(f"{self.employee_id},{self.name},{self.role},{self.salary}")

#function add_employee(), read_employees()

    def add_employee(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

        with open("employees.txt", "a", encoding="utf-8") as file:
            file.write(f"{self.employee_id},{self.name},{self.role},{self.salary}\n")
        

    def read_employees(self):
        try:
            with open("employees.txt", "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("The file 'employees.txt' does not exist")
             

# file creation context manager
with open("employees.txt", "w", encoding="utf-8") as file:
    file.write("EmployeeID,Name,Role,Salary\n")
print("Base file created with headers.")


# Employee data inside a  list of key value pair dictionaries
employee_data = [
    {"id": 101, "name": "Rahul", "role": "Python Developer", "salary": 50000},
    {"id": 102, "name": "Anjali", "role": "Tester", "salary": 45000},
    {"id": 103, "name": "John", "role": "Developer", "salary": 60000},
    {"id": 104, "name": "Priya", "role": "Tester", "salary": 48000}
]

# for Loop through the data and write to file
all_employees = []
for data in employee_data:
    emp = Employee()
    emp.add_employee(data["id"], data["name"], data["role"], data["salary"])
    all_employees.append(emp)
print("Employee records successfully updated in the file.")

#Printing the read content 
print("\nReading File Content:")
emp.read_employees()
#displaying the employee details content 
print("\nDisplaying Employee Details Content:")
for emp in all_employees:
    emp.display_details()

#calculating the highest salary 
def find_highest_salary(employees):
    highest = max(employees, key=lambda emp: emp.salary)
    print(f"\n Highest Salary: {highest.name} (₹{highest.salary:,.2f})")
    return highest
find_highest_salary(all_employees)

#calculate salary>50000 
def find_salarygreater(employees):
    findsalarygreater = [emp for emp in employees if emp.salary > 50000]
    print(f"\n Salary Greater than>50000: ")
    for emp in findsalarygreater:
        print(f" - {emp.name}: {emp.salary:,.2f}")
find_salarygreater(all_employees)

#count employee by role    
def find_employees_by_role(employees):
    role_counts = {}
    for emp in employees:
        role_counts[emp.role] = role_counts.get(emp.role, 0) + 1

    print("\nEmployee Count by Role:")
    for role, count in role_counts.items():
        print(f"   - {role}: {count}")
    return role_counts
find_employees_by_role(all_employees)