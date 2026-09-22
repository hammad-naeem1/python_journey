# ===================
# class variable 
# ================
# --------
# shared among all instenses of a class 
# defined outide the costucator
# allow you to share data among all object created fro that class 
# ----------------------

class Student:
    class_year=2026
    num_student=0
    def __init__(self ,name ,age    ):
        self.name=name
        self.age=age
        Student.num_student+=1
student1=Student('hammad',16   )
student2=Student('barhajn',10   )
student2=Student('irfan',10   )
# print(student1.name)
# print(student1.age)
# print(Student.class_year)
# print(Student.num_student)
print(f' my graduagting class :{Student.class_year} and class studets :{Student.num_student}')