import statistics
students=[]
marks=[]
print("===== Student Grade Manager =====")
while True:
    option=input('''

1. Add Student
2. Show Students
3. Search Student
4. Show Statistics
5. Exit

Enter your choice:''')
    if option=="1":
        student=input(" enter student name !")
        while True:
            try:
                while True :
                  mark=int(input("Enter student marks !"))
                  if mark>=101 or mark<=0:
                      print(" please enter a num betwwen 100")
                  else:
                      break
            except ValueError:
                print(" enter a number !")
            else:
                break 
        students.append(student)
        marks.append(mark)
    elif option=="2":
        if not students:
            print(" no record  of student!")
        else:
            student_data=zip(students,marks)
            for student,mark in student_data:
                print(f" student name is {student} and mark is {mark}")
    elif option=="3":
        search=input(" enter student for search").lower()
        if search not in students:
            print(" student not found!_")
        elif search in students:
            index=students.index(search)
            print(f" student name is {students[index]} and mark is {marks[index]}")
    elif option=="4":
        if not students:
            print("no record ")
        else:
            x=statistics.mean(marks)
            print(f" avg of student is _{x}")
            a=(min(marks))
            b=(max(marks))
            print(f" the highiest mark is {b}_from class_")
            print(f" the lowest mark is {a}_from class_")
    elif option=="5":
        print(" thannks for using our program !")
        break
    else:
        print(" enter a valid option")
        
