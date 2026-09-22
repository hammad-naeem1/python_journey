# 
#===========================
# iterrable  objects  
# ============================
# an object capable of returning 
# its members one at a time. 
# Examples include all sequence types
# (such as list, str, and tuple) 
# and some non-sequence types like dict, file objects,
# and objects of any classes you define 

# =========================================================

# -----
# dictonary
#------
my_dictonary={"a":1, "b":1,  "c":3,  "d":4  }
for key,value in my_dictonary.items():
    print(f"{key}:{value}")





# ==========================================

# example :
num=[1,2,3,4,5,]
# list are iterrable
# so we can use them in a loop for one by one 
for numm in num:
      print(numm ,end=" " )

# =========================================

nummm=(1,2,3,4,5,)
# # tuples  are  also iterrable
# # so we can use them in a loop for one by one 
for numm in nummm:
    print(numm, end=" " )


# =========================================

fruits={"apple","banana","coconut","mango"}
# # sets   are  also iterrable
# # so we can use them in a loop for one by one 
for fruit in fruits:
     print(fruit , end=" ")

