score=0
print('''         ================================
             WELCOME TO QUIZ GAME : 
         ================================                 ''')
name=input(" what is your name sir ??__")
while True:
    try:
     age=int(input(" what is your age ??__"))
    except ValueError:
        continue
    else:
       break
if age<=14:
    print(" sorry ,  your a minor !!")
    exit()
elif age>=25:
    print(" sorry ,  your too old  !!")
    exit()
else:
    pass

questions=["who is the prime minister of pakistan?"," who is the ceo of anthropic",
           "who won the world up of 2026"]

print("          ")
print(questions[0])
print('''your options are::
A , shehbaz_sharif
B , imran_khan
C , maryam_nawaz
D , bilawal_bhutto''')
ans1=input(" chosee your option__")
if ans1=="a":
    print(" coorect ✅ ")
    score=score+1
else:
    print(" wrong option")


print("          ")
print(questions[1])
print('''your options are::
A , bill gates
B , mark_zukerberg
C , sam_altman
D , elon musk''')
ans2=input(" chosee your option__")
if ans2=="c":
    print(" coorect ✅ ")
    score=score+1
else:
    print(" wrong option")
print("                 ")
print(questions[1])
print('''your options are::
A , spain
B , real_madrid
C , portugal
D , argentina''')
ans3=input(" chosee your option__")
if ans3=="a":
    print(" coorect ✅ ")
    score=score+1
else:
    print(" wrong option")
print(f'''
name__{name}
age__{age}
score___/{score}''')


