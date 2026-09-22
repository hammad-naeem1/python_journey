name=input(" kindly enter your good name :")
print(" hello mr ::", (name))
w =int(input("kindly enter your age please ::"))
if w   >=6 and w <=21:
        print(" so your age is " ,+(w))
else:
    print("sorry ; we dont have this old student in our school ")
    exit()
p=int(input("can you please enter your Roll number ::"))
print(" student no 43: Roll number:" ,+ (p))
print(" student==",name)


import statistics
while True:
    try:
        math=int(input(" what is your math num ??"))
        science=int(input(" what is your math num ??"))
        english=int(input(" what is your math num ??"))
        print(" your average would be !!")
    except ValueError:
         pass
    else:
        break
print(statistics.mean([ math, english,science,]))


score=int(input(" can you please enter your  parcentage score: "))

if score >= 90 and score <=100:
    print(" your grade is ➡️ Grade : A :: Well DONE  you can move to next class !! ")

elif score >= 80 and score < 90 :
    print(" your grade is ➡️ GRADE : B :: Well DONE  you can move to next class !!")

elif score >= 70 and score < 80 :
    print(" your grade is ➡️ GRADE : C ::you can move to next class but need Improvement")

elif score >= 60 and score < 70:
    print(" your grade is ➡️ GRADE : D ::you can move to next class but need Improvement ")

elif score >= 1 and score < 60:
    print("  your grade is ➡️ GRADE : F : :: your failed !! leave our school !!! we dont nedd loser leave our school")

else:
     print(" kindly enter your correct grade parcentage ")



