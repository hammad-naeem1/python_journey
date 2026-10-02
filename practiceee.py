import statistics
student_name=[]
student_mark=[]



for student  in range(3):
    student=input('enter stdudent name_')
    mark=int(input("enter your mark "))
    student_name.append(student)
    student_mark.append(mark)
students=zip(student_name,student_mark)
for student,mark in students:
    print(f" student |{student}|marks|{mark}")
print(f" class min marks|{min(student_mark)} _ class highest mark |{max(student_mark)}| ")
print(f"average of class|{statistics.mean(student_mark)}")


