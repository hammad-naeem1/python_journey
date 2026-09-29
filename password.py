# This is my second working and useful code
#  after one and half week of python learningpit
pin=1234
def pass_word():
   while True:
      input=int(input("kindly enter your pin !!"))

      if input==pin:
         print("login access granted ✅ !!")
         
      elif  input!=pin:
         print(" plzz enter corret pin")
         
      
      else:
         print(" plz enter correct !")
               
pass_word()