# ================================
# object 
#============
# is a bundle of data and methods that operate on that data. 
# In Python, everything is an object, including numbers, strings, functions,
# and even classes themselves. Objects are instances of classes, which define the structure
# and behavior of the objects.

# ==================
# class
# ======================== 
# is a blueprint for creating objects.
#  It defines the attributes (data) and methods (functions)
#  that the objects created from the class will have. 
#  A class can be thought of as a template for creating objects.




# from cars import car
# car1=car('bmw',2025,'black',False)
# car2=car('mustang',2021,'black',True)
# # print(car1.model)
# # print(car2.year)
# # print(car1.color)
# # car1.stop()
# # car1.drive()
# car1.describe()
# car2.describe()

from classandobjects import student
student1=student("hammad",20)
student1.introduce()
student2=student("barhjan",21)
student2.introduce()
student1.greet()