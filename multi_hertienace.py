# multiple_inhertance_
#                     inherent more than one class

# multilevel_inhertance_
                        # inhenert from a parent which inherent from another parent 

class animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f'{self.name}  is eating')
    def sleep(self):
        print(f' {self.name} is sleeping')


class prey(animal):
    def flee(self):
        print(f' {self.name} is felling')

class predator(animal):
    def hunt(self):
        print(f' {self.name} is  hunting')


class rabbit(prey):
    pass


class hawk(predator):
    pass



class fish(prey,predator):
    pass
rabbit=rabbit('bugs')
hawk=hawk('tony')
fish=fish('nemo')

rabbit.sleep(),rabbit.eat(),fish.hunt()