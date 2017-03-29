import os
# Dictionaries for students
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
# Defining functions and methods
def average(x):
    total = sum(x)
    aver = float(total) / len(x)
    return aver
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
print(get_average(lloyd))
print(get_letter_grade(get_average(lloyd)))
students = [lloyd, alice, tyler]
def class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
# displaying the calculated marks average and grade
print(class_average(students))
print(get_letter_grade(class_average(students)))
#Asking the users if they want to run the file again or Go to main men or Exit the Program
print("Enter 0 to Play again or 1 to got to Main Menu or 2 to exit or Terminate the program")
option_selected_by_user=int(input("My option is : "))
if option_selected_by_user==0:
    print("Battleship Will be started again")
    os.system('python students_to_teacher.py')
elif option_selected_by_user==1:
    print("Redirecting to Main Menu")
    os.system('python main.py')
elif option_selected_by_user==2:
    exit()
else:
    os.system('python main.py')
