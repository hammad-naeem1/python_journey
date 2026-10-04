class school:

    def get_info(self):
         print(f" the name:{self.name} and is_alive{self.is_alive}=")



class student(school):
    def __init__(self,name,is_alive,):
        self.name=name
        self.is_alive=is_alive



class teachers(school):
        def __init__(self,name,is_alive,is_present):
            self.is_present=is_present

class class_rooms():
     def __init__(self,brand,color):
          self.brand=brand
          self.color=color

student1=student('hammad',True)

student1.get_info()