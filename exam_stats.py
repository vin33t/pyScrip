import os
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def print_grades(grades):
    for grade in grades:
        print(grade)
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    result = variance / len(scores)
    return result
print(grades_variance(grades))
def grades_std_deviation(variance):
    result = variance ** 0.5
    return result
print(print_grades(grades))
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(grades_variance(grades)))
#Asking the users if they want to run the file again or Go to main men or Exit the Program
print("Enter 0 to Play again or 1 to got to Main Menu or 2 to exit or Terminate the program")
option_selected_by_user=int(input("My option is : "))
if option_selected_by_user==0:
    print("Battleship Will be started again")
    os.system('python exam_stats.py')
elif option_selected_by_user==1:
    print("Redirecting to Main Menu")
    os.system('python main.py')
elif option_selected_by_user==2:
    exit()
else:
    os.system('python main.py')
