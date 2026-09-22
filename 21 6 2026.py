
print(" welcome sir to UBL ATM machine  💳💳")
balance=37600

cardnumber=int(input("PLEASE enter your card information  ::"))
if cardnumber==51102:
    print(" YOUR card number is valid ✅")
else:
    print('''card number is invalid please enter a valid one 🚨🚨
          you will get only three chance !!!!
          other wise your card will be blocked !! remember sir  ⚠️⚠️''')
    exit()

menu=input(" please enter M for menu ::").upper()

m=input(" please enter D for deposit, W for widraw, C for checkbalance ::").upper()



if m=="C":
    print("your current balance is ::➡️➡️➡️", balance)
    s=input(''' to widraw or deposit !!!
             please insert your card  again in ATM sir !!
            here is your resipt !!! 
            please press ENTER !! ::''')
    print(" hope you enjoyed our servies !!  please come again sir  👋👋")

elif m=="D":
   g=int(input("how much money you want to deposit sir ? ::"))
   print("here is your current balance sir ➡️➡️", g+balance)
   x=input(" thanks for using our atm , please enter e for exit  ::")
   print(" hope you enjoyed our servies !!  please come again sir  👋👋")



elif m=="W":
   q=int(input("how much money you want to widraw   sir ? ::"))
   print("here is your current balance sir ➡️➡️", balance-q)
   e=input(" thanks for using our atm , please enter e for exit  ::")
   print(" hope you enjoyed our servies !!  please come again sir  👋👋")

else:
    print("please enter a valid option sir  form menu !!  🚨🚨")


