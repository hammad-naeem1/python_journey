# ========
# # list comprehension
# =====================
# # e.g 
# # a consise way to create lists in Python. 
# # It allows you to generate a new list by
# # applying an expression to each item 
# # in an existing iterable (like a list, tuple, or string)
# # and optionally filtering items based on a condition.
# ============================================================


grades=[32,98,65,92,98,23,2]
passing_grades=[grade for grade in grades if  grade>=60   ]
print(passing_grades)









# doubles=[x*2 for x in range(1,11)]
# print(doubles)
# triple=[x*3 for x in range(1,11)]
# print(triple)
# square=[x*x for x in range(1,11)]
# print(square)



# students=["barhajan","jallel","irfan"]
# students=[student.upper()      for student in students]
# print(students)


# numbers=[1,-2,-3,-4,-5,-6]
# postive_num=[num for num in numbers   if num>=0]
# negative_num=[num for num in numbers   if num<0]
# print(negative_num)
