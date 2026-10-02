while True:
    guess=input(' wanna play even /odd game ? yes/no _')
    if guess=='yes':
            while True:
                try:
                    num=int(input(' enter your num ! '))
                except ValueError:
                    print(' enter a num !')
                else:
                    break
            if num%2==0:
                print(' your num is a even')
            else:
                print(' your num is odd')
    elif  guess=='no':
         print(' thanks for trying our program ')
         break
    else:
         print(' enter a valid command')
