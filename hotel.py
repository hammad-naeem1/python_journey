print('''
========================
 Welcome  to our hotel sir !!🏨🏨
===================================''')

#  i have made this when i was bored i never knew
# this will gonna work hh anyways


name=input(" what is your good name sir ? ::")
while True :
    menu=input(''' This is our menu sir 
                1. Standard Room = 5000 PKR
                2. Deluxe Room = 8000 PKR
                3. Suite = 12000 PKR                     
                4 . quit
                what you want sir ????                  '''  )
    if menu==1:
        x=input("how much night you will stay sir ? ")

    elif menu==2:
        x=input("how much night you will stay sir ? ")


    elif menu==3:
        x=int(input("how much night you will stay sir ? "))
    

    else:
        print(" kindly chosee something which is in menu")
        
        
    w=input("ohh !!  we hope you will enjoy !! :: you also want breakfast sir ??")
    if w=="yes":
        q=input(" you want airport pickup sir ?? ")

    print(" ok then here is your Bill sir !!")
    print(" costumer =", name)
    if menu=="standard room":
        print('''           BILL                                      
            standard room  = 5000 RS    
            airportpickup free !!
            days gonna stay =''',x)
        print(" your total BIll is = 6500 per night  ")
        print(''' hope you enjoyed our servises 
                                                            
            PLEASE COME AGAIN SIR 👋👋                     
                                                OUR Helpline = 432                ''')

    elif menu=="deluxe room":
        print('''           BILL                                      
            Deluxe room  = 8000 RS    
            airportpickup free !!
            days gonna stay =''',x)
        print(" your total BIll is = 9500 per night  ")
        print(''' hope you enjoyed our servises 
                                                            
            PLEASE COME AGAIN SIR 👋👋                     
                                                OUR Helpline = 432                ''')

    elif menu=="suite":
        print('''           BILL                                      
            suite room  = 12000 RS    
            airportpickup free !!
            days gonna stay =''',x)
        print(" your total BIll is = 13500 per night  ")
        print(''' hope you enjoyed our servises !!
                                                            
            PLEASE COME AGAIN SIR 👋👋                     
                                                OUR Helpline = 432                ''')
    