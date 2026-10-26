# Student Marks Management System

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