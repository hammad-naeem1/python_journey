# # super()
# super class is the fucntion used in a child class to call method from a parent class (super_class)
# allows you to extened the functionality of the inhetiend method


class shape:
      def __init__(self,color,is_filled):
            self.color=color
            self.is_filled=is_filled
      def describe(self):
       print(f"your shape  is {self.color} and {'filled'if self.is_filled else 'not filled'}")
 

class circle(shape):
    def __init__(self,color,is_filled,radius):
       super().__init__(color,is_filled)
       self.radius=radius
    def describe(self):
          super().describe()
          print(f"it is a circle which area is {3.14 * self.radius * self.radius  }cm")
         
class square(shape):
        def __init__(self,color,is_filled,wight):
            super().__init__(color,is_filled)
            self.wight=wight
    
 
class triangle(shape):
     def __init__(self,color,is_filled,wight,height):
                  super().__init__(color,is_filled)
                  self.wight=wight
                  self.height=height

circle=circle(color='red',is_filled=True,radius=5)
square=square(color='blue',is_filled=False,wight=8)
triangle=triangle(color='yellow',is_filled=False,wight=9,height=8)
circle.describe()
