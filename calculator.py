print("Welocme to the calculator 📲📲")

# This is my first working and useful code
#  after one week of python learning

a=int(input(" PLEASE enter your first num, "))
b=int(input(" PLEASE enter your second num, "))
c = input("Enter A for +, S for -, M for *, or D for /: ").upper()


A=a+b
S=a-b
M=a*b
D=a/b


if c== "A":
   print("the SUM of your  first and second numerical  is ➡️ ::", A)

# i have added (elif )(else)and (if ) later the first version was diffrenet


elif c== "S":
   print("the DIFFERENCE of your  first and second numerical is  ➡️::",S )


elif c== "M":
   print("the PRODUCT of your  first and second numerical is  ➡️::",M )


elif c== "D":
   print("the DIVISION of your  first and second numerical is  ➡️ ::", D)


else:
   print("Please enter a valid operator🚨⚠️ ")
