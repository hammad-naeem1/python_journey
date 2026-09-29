students=[]
marks=[]
for  _ in range(3):
    while True:
            studenet=input(' enter studnet name ?')
            students.append(studenet)
            mark=int(input(' enter the marks'))
            marks.append(mark)
            if mark>100 or mark <0:
                  print('enter correct marks')
            else:
                  break
option=input(' do you wanna see studnets ?')
while option=="yes" :
    if not studenet:
      print(' no record ')
    else:
        all_record=zip(students,marks)
        for student,mark in all_record:
                                print(f" students|{studenet}|marks|{mark}|")
                        
    break