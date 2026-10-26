# Student & Employee Management Workspace

Python applications designed to process structural data ,files and displays records efficiently.

## Repository Directory Structure

📁 python-milestone-assesment/
├── 📁 .pytest_cache              # pytest cache files to run test
├── 📁 Question1/
│   ├── main.py
│   └── README.md                  # Detailed student module 
│
└── 📁 Question2/
    ├── main.py
    └── README.md                  # Detailed employee module 

### 1️⃣ Student Marks Management System
Python application designed to accept details of multiple students, calculate their results, manage and display a student academic marks summary based on subject scores.

## Problem Statement
Project scope require automated workflows to process individual student marks details efficiently. 

This program solves this requirement by:
* Storing attributes for each student: `StudentID`, `StudentName`, `PythonMarks`, `SQLMarks`, and `AIMarks`.
* Calculating aggregate evaluation metrics: **Total Marks**, **Average Marks**,**Grade**.
* Determining qualifying criteria status: **PASS** (Average Score >40) or **FAIL** (Average Score < 40).
* Evaluating performance metrics: Tracking the highest-scoring individual and identifying students maintaining an average score exceeding 75%.

##  Approach & Logic
The codebase developed by using python programming methodology 
1. **Data**: Individual data are encapsulated inside key value pair dictionaries, grouped globally in outer list container.
2. **Functions**: Functions evaluate individual tasks (`total_marks`, `calculate_average`, `get_grade`, `check_result`). This eliminates calculations redundancy.
3. **Lookups**: Uses Python's native `max()` higher-order function equipped with a custom sorting `lambda` key expression to extract top-performers
4. **Filtering**: List Comprehensions to execute functional array mapping and filters concurrently.

##  Python Concepts Used
* **Lists & Dictionaries**: Grouping structured document items using a list block populated with key-value pairs.
* **Functions**: Evaluating logic by accepting variables and explicitly returning calculated result.
* **Conditions & Iteration Loops**: Conditional logic (`if-elif-else`) alongside structural `for` elements.
* **List Comprehension**: Applying concise element mapping pipelines to filter elements dynamically.
* **Output String Formatting**: Customizing string rendering configurations i.e standard `f-strings`, trailing decimal precision masking (`:.2f`), and clean delimiter connections (`.join()`).

##  How to Run the Program

### Prerequisites
Make sure you have Python 3.x and pytest installed on your machine.

### Step-by-Step Execution
1. Open **Visual Studio Code**.
2. Create a new file named `main.py`.
3. write your Python script code inside the file and save it.
4. Open the built-in terminal window 
5. Run the file using the following command from Question1 folder:
      pytest main.py -v -s 
   
### Sample Input Data
students_list = [
    {
        "StudentID": 101,
        "StudentName": "Rahul",
        "PythonMarks": 90,
        "SQLMarks": 90,
        "AIMarks": 90
    },
    {
        "StudentID": 102,
        "StudentName": "Anjali",
        "PythonMarks": 90,
        "SQLMarks": 90,
        "AIMarks": 80
    }
]

### Sample Terminal Output
StudentID: 101
Name: Rahul
Total: 270
Average: 90.00
Grade: A
Result: PASS
--------------------
StudentID: 102
Name: Anjali
Total: 260
Average: 86.67
Grade: B
Result: PASS
--------------------
Highest Scoring Student: Rahul

Students above Average > 75 : Rahul, Anjali
### 2️⃣ Employee File Management System

A Python-based Employee Record Management System application manages employee information, store data to a text file and generate a report

## Problem Statement
The project requirement is to build a system that records employee data:
1. Initialize a data storage file with appropriate column headers.
2. Add multiple employee records (ID, Name, Role, and Salary)
3. Save the records persistently to a text file (`employees.txt`) using a comma-separated format.
4. Read and display the contents of the file.
5. Provide the information from the employee dataset:
   - Identify the employee drawing the highest salary.
   - Filter and display employees earning more than a specific benchmark (₹50,000).
   - Compute the aggregate head-count of employees grouped by their  roles.

## Approach / Logic Used
* **OOPS:** The system models employee entity using a class (`Employee`). Each employee's data are mapped directly to instance attributes.
* **Bulk Loop Processing:** Instead of manually writing duplicate code blocks for each separate employee object, the program structures the employee input data inside a list of dictionaries and processes it sequentially within a single `for` loop.
* **File Operations:** Utilized text writing logic (`file.write`)
* **Data Reduction & Analysis:** 
  - **Highest Salary:** Uses `max()` utility paired with a custom key evaluation (`lambda`) to pull the employee object containing the maximum salary value in a single pass.
  - **Salary Filtering:** Uses list comprehension to dynamically extract elements matching a conditional threshold (`emp.salary > 50000`).
  - **Role Distribution Aggregation:** Dictionary along with the safely executed `.get(role, 0)` dictionary pattern to dynamically map frequencies of unique positions.

## Python Concepts Used
The project uses python based capabilities:
* **Class & Object:** Defined the Class (`class Employee:`) and initialized instances.
* **Constructor & Method:** Defined initialization (`__init__`) alongside action methods (`add_employee`, `display_details`, `read_employees`).
* **Context Manager:** Used (`with open(...) as file:`) to protect file writing blocks.
* **File Handling:** Handled text file - write mode (`"w"`), append mode (`"a"`), and read mode (`"r"`).
* **Exception Handling:** Handled using a `try...except FileNotFoundError:`.
* **Functions:** Defined functions (`find_highest_salary`, `find_salarygreater`, `find_employees_by_role`).
* **Lists & Dictionaries:** Implemented lists (`all_employees`) for iteration queues and a dictionary (`role_counts`) for frequency mapping.and employee data for employee information.
* **Code Readability:** Applied descriptive labels, and function docstrings.

## How to Run the Program

### Prerequisites
* Ensure **Python 3.x** and pytest is installed on your machine.

### Execution Steps
1. write the code into a `main.py` file.
2. Open your terminal interface in VSS code.
3. Navigate to the folder containing your script:
4. Run the application script using the pytest interpreter:
      pytest main.py -v -s 
5. The application will run according to the logic written and create/update the `employees.txt` file in the exact same workspace directory.

## Sample Input
Structured data dictionary inputs:

employee_data = [
    {"id": 101, "name": "Rahul", "role": "Python Developer", "salary": 50000},
    {"id": 102, "name": "Anjali", "role": "Tester", "salary": 45000},
    {"id": 103, "name": "John", "role": "Developer", "salary": 60000},
    {"id": 104, "name": "Priya", "role": "Tester", "salary": 48000}
]

## Sample Output
Running the script generates the following  output in terminal:

Base file created with headers.
Employee records successfully updated in the file.

Reading File Content:
EmployeeID,Name,Role,Salary
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000


Displaying Employee Details Content:
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000

 Highest Salary: John (₹60,000.00)

 Salary Greater than>50000: 
 - John: 60,000.00

Employee Count by Role:
   - Python Developer: 1
   - Tester: 2
   - Developer: 1   