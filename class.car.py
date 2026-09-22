class vechaile:
    def __init__(self,colour,model):
        self.colour=colour
        self.model=model

    def drive(self):
        print(f' your driving {self.model} : {self.model}')

class car(vechaile):
   def start(self):
       print(f" your   {self.colour} car : {self.model}  engine is on")
      

class motorcycle(vechaile):
    def start(self):
       print(f" your  {self.colour}  motorcycle : {self.model}  engine is on")
      
car=car('yellow',2011)
motorcycle=motorcycle('yellow',2011)

print(car.colour,car.model)
car.start()
motorcycle.start()