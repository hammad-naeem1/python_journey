import statistics
student_name=[]
student_grade=[]
student_mark=[]



for student  in range(5):
    student=input('enter stdudent name_')
    grade=input("enter your grade ")
    mark=int(input("enter your mark "))
    student_name.append(student)
    student_grade.append(grade)
    student_mark.append(mark)
students=zip(student_name,student_grade,student_mark)
for student,grade,mark in students:
    print(f" student |{student}|grade|{grade}|marks|{mark}")
print("")
b=(min(mark)) 
a=(max(mark)) 
c=statistics.mean(mark)
print(f" class min marks|{b} _ class highest mark |{a} ")
print(f"average of class|{c}")


