# polymorpism =
# to have many forms or faces

# two ways to achive polymorpsim 
# =======
        # inherience=an object can be treted same as type parent class
        # ducktyping=object must have nesscary attribute/methods
# ============
# inherteince way +
# =================

from abc import ABC ,abstractmethod
class shape:
    @abstractmethod
    def area(self):
         pass


class circle(shape):
        def __init__(self,radius):
           self.radius=radius
        def area(self):
             return 3.14 * self.radius **2
class square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
         return self.side ** 2 

    

shapes=[circle(7),square(2)]
for shape in shapes:
     print(f'''area is {shape.area()}    ''')



# ============
# duck typing
# =========

# it is the way to achive polymorpism beside inhertience 
# object must have the minimum nessacary Attribute/methods
# ======
# --which means if it has some simlartyes that program would consider it too !
# ===



class animal:
     alive =True

class dog(animal):
     def speak(self):
        print(' woff')

class cat(animal):
    def speak(self):
     print(' meoww')
# ==
# exampple
# ===

class car:
    def speak(self):
         print(' hownkk ')
    

animals=[dog(),cat(),car()]
for animal in animals:
    animal.speak()

    