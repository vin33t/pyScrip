import os
#printing the available options
print("Enter the file Number you want to run")
print("Enter 1 for Students to Teacher")
print("Enter 2 for Battleship")
print("Enter 3 for Exam Statistics")
print("Enter 0 to exit")
option_selected_by_user=int(input("I want to Run: "))
#redirecting the user based on the input
if option_selected_by_user==1:
    print("You selected Student to Teacher as your Option")
    os.system('python students_to_teacher.py')
elif option_selected_by_user==2:
    print("You Selected Battleship as your Option")
    os.system('python battleship.py')
elif option_selected_by_user==3:
    print("You selected Exam Statistics as your Option")
    os.system('python exam_stats.py')
elif option_selected_by_user==0:
    exit()
else:
    os.system('python main.py')

