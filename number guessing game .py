import random

print('''---------------------------- 
      number gueesing game
------------------------------   ''')
attempt=0
num=random.randint(1,100)
while True:
    while True:
        try:
            guess=int(input(" what is the number  ?_"))
            attempt+=1
        except ValueError:
             print(" please enter a number")
        else:
             break
    if guess>num:
         print(" too high")
    elif guess<num:
        print(" too low")
    elif guess==num:
         print("correct ! ") 
         break
    else:
        print(" kindly enter a num betwwen 1 to 100")

print(" congrats ! you did it !")
print("")
print(f"your attempts __{attempt}")

