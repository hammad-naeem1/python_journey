

# ===============================

#     ARBOTARY ARGUMENT 

# ===============================

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
    


def sum(*args):
    sum=0
    for i in args:
        sum= sum +i
    return sum

print(sum(567,67,5678,678,678,23,23))




def my_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
my_details(name="hammad", age=30, city="New York")


def shopping_label(*args,**kwargs):
    for arg in args:
        print(arg ,end=" ")
    print()
    for key,values in kwargs.items():
        print(f"{key}:{values}")

shopping_label("hammad","naeem","barahjan","kilo",
               city="karachi",
               contuty="pakistan",
               zip="98810")







              