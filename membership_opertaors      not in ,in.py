
# ========================================================


# membership operators are used to test whether a value
# or variable is found in a sequence
# (such as a string, list, tuple, set, or dictionary)
#  The two membership operators in Python are:

#    (    # not in     ),(  #  in  )


# e .g 


email="hammad123@gamil.com"
if  "."in email and "@" in email:
    print(" valid email")
else:
    print(" invalid email")






# students={"barhajan","jallel","irfan"}
# while True :
#     name=input("  enter student name !")
#     if name not in students:
#         print(" student not found !")
#     elif name in students:
#         print(f"{name} was founded  ! ")





# while True :
#     marks={"hammad":90,"barahjan":23,"ebad":65 }
#     name=input("  enter student name !")
#     if name in marks:
#         print(f"{name} was found ! {marks[name]} is marks")
#     elif name in marks:
#         print(f"{name} was  not founds")
#     else:
#         print(f" {name} not found ")


# ========
while True :
    marks={"hammad":90,"barahjan":23,"ebad":65 }
    name=input("  enter student name !")
    if name not in marks:
         print(f"{name} was  not founds")
    elif name in marks:
        print(f"{name} was found ! {marks[name]} is marks")       
    else:
        pass







# ===========================================================
# -------------
#   e.g
#         in :
# while True :
#     word="apple"
#     letter=input(" guess the secet word !")
#     if letter==word:
#             print(f" yes the word is {letter}")
#             break
#     elif letter in word:
#         print(f" there is a :{letter}  ")
#     else:
#         print(f"{letter} was not found !")

# -------------



# ===========================================================
# -------------
#   e.g
#        not  in :
# while True :
#     word="apple"
#     letter=input(" guess the secet word !")
#     if letter==word:
#             print(f" yes the word is {letter}")
#             break
#     elif letter  not in word:
       
#         print(f"{letter} was not found !")
#     else:
#         print(f" there is a :{letter}  ")
# # -------------







