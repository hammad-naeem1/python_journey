import sys
number=45
while True:
    try:
        guess=int(input(" what is the secert number__"))
    except ValueError:
        print(" please enter a valid number__")
        continue
    if number<guess:
        print(" this is higher than the secert number__")
    elif number>guess:
        print(" this is lower than the secert number__")
    else:
        print(" you got it right__")
        break
