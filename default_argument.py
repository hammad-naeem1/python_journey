# ----------------------------------------------------------------------------------
#         DEFAULT ARGUMENT IN PYTHON
# 

# A default argument in Python allows a function parameter to take a predefined value
# if no argument is provided during the function call.

# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
#     postional Argument :
    
      #  you have to maintain position of the argument in the function call.
     
        # example :            
          #     def greet(name, age=30):
          #         print(f"Hello {name}, you are {age} years old.")

          #     greet("Alice")  # Output: Hello Alice, you are 30 years old.
          #     greet("Bob", 25)  # Output: Hello Bob, you are 25 years old.
# ---------------------------------------------------------------------------------


# # ----------------------------------
# #         # default Argument
# def net_price(list_price ,  (  ➡️  discount=0 , tax=0.05)⬅️: #these are the egualt 
                                                                # value in fuction like stoted  )                
#         return list_price *(1-discount) * (1+tax)
# o=input("ener the list price : ")
# print(net_price(float(o)))
# # -----------------------------------




# ============================================================

# # *args
# =========
# #          allow you to passs non- multiple key arguemnt
# e.g
# def num(*args):
#     total=0
#     for arg in args:
#       total += arg
#     return total
# print(num(8,9,0))  
# ------------------------------

# def display_name(*args):
#     for arg in args:
#         print(arg , end=" ")
# display_name("hammad",'naeem')


# ==============================================
# # **kwargs
# =================
# #         allow you to passs multiple key arguemnt
#           # unpacking opreator


# def print_adrees(**kwargs):
#     for key, value in kwargs.items():
#         print(f" {key} :{value}")
# print_adrees(city="karachi",
# country="pakistan",
# distict="keech")
    


















# ============================================================