
students={}
while True :
    name=input("what is your name _((q to quit)")
    marks=int(input("what are  your marks _(0 to quit)"))
    if name=="q"and marks==0:
        break
    else:
        students.update({name:marks})

students.items
for key , item in students.items():
    print(f'student_{key}: marks_{item}')
