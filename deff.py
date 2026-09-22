def area():
     areaa={}
     while True :
        try:
            length=int(input("input your length :"))
            weight=int(input("input your weight :"))
        except ValueError:
            print(" enter a int please ! :")
        else:
            break
     a=length * weight
     print(f" your calculated area is __ {a}")
     while True :
         option=input(" you want to save your? area ? yes / no_")
         if option=="yes":
            key=input(" what  is your key ? ")
            areaa.update({key: a})
            break
         elif option=="no":
             print(" ok sir !")
             print(f" your calculated area is __ {a}")
             break
         else:
             print(" sir please enter a valid option")
area()

