#Store data as key value pairs using List and Dictionary
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
#Functions to calculate 
def total_marks(student):
    return student["PythonMarks"] + student["SQLMarks"] + student["AIMarks"]

def calculate_average(student):
    return total_marks(student) / 3

def get_grade(student):
    avg = calculate_average(student)
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "D"

def check_result(student):
    if calculate_average(student) >= 40:
        return "PASS"
    else:
        return "FAIL"
   
#Method to display details
def display_details(student):
    print(f"StudentID: {student['StudentID']}\n"
          f"Name: {student['StudentName']}\n"
          f"Total: {total_marks(student)}\n"
          f"Average: {calculate_average(student):.2f}\n"
          f"Grade: {get_grade(student)}\n"
          f"Result: {check_result(student)}\n"
          f"{'-'*20}")
    #to display the student details based on input data     
for student in students_list:
    display_details(student)

    #print(display_details(students_list))
    #print(f"Highest Scoring Student: {top_student['StudentName']}\n")

#Calculate the Highest scoring student and average above 75 using max,lambda list comprehension
top_students_above_75 = [x for x in students_list if calculate_average(x) > 75]

#if top_students_above_75:
  # for student in top_students_above_75:
   #    display_details(student)
#else:
  # print("\nNo students found with an average score greater than 75.")

top_student = max(students_list, key=lambda x: calculate_average(x))
print(f"Highest Scoring Student: {top_student['StudentName']}\n")
names = [student["StudentName"] for student in top_students_above_75]
print(f"Students above Average > 75 : {', '.join(names)}")    