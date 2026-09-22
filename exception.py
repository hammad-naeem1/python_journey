
# # print(" hello, world)
# while True:
#     try:
#      x=int(input(" what s x ?"))

#     except ValueError:
#      print(" please type  a integar ")
#     else:
#       break

# print(f" x is {x}")








print(" welcome to the calculator")
while True:
    try:
      num1=int(input(" what s the num1??"))
      num2=int(input(" what s the num2??"))
      operator=input(" enter an opetaror among these ,+ ,-,/,*__")
    except ValueError:
         pass
    else:
        break
if operator=="+":
        print(num1+num2)
        
elif operator=="-":
      print(num1-num2)
  
elif operator=="/":
        print(num1/num2)
    
elif operator=="*":
        print(num1*num2)
    
else:
    print(" please enter a valid operator")
