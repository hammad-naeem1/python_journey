import statistics
students=[]
marks=[]
avg=[]
while True:
   student=input(" enter student name !! or (q to quit)__")
   if student=="q":
    break
   else:
        while True:
            try:
                mark=int(input("enter your markrs !!"))
                while True:
                  if mark < 0 or mark > 100:
                   print(" please enter the marks between 0 and 100:")
                   break
                  else:
                   break
            except ValueError:
                print(" please enter a float or a int ")
            else:
                break
        students.append(student)
        marks.append(mark)
        avg.append(mark)

print('''         ================================
         Here ARE YOUR RESULT
         ================================                 ''')
average=statistics.mean(avg)
avg=average
for x in range(len(students)):
    if marks[x]>=50:
        print(f"name: {students[x]}, marks: {marks[x]}, status: Pass")
    elif marks[x]<50:
        print(f"name: {students[x]}, marks: {marks[x]}, status: Fail")
print(f"average marks of the class is: {avg}")

