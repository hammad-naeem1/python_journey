# inhertiance=allow a  class inhert Attribute and methods from another class
#             helps a code reuseablity and extensiblity
#             class child(parent)


class animals:
    def __init__(self,name):
        self.name=name
        self.is_alive=True



    def eat(self):
        print(f"{self.name} is eating ")
    

    def sleep(self):
        print(f"{self.name} is sleeping ")


class dog(animals):
    def speak(self):
        print('woff')

class cat(animals):
    def speak(self):
            print('meow')
    


class mouse(animals):
    def speak(self):
            print('squek')
    

dog=dog('barahjan')
cat=cat('tenger')
mouse=mouse('hammad')

print(dog.name,cat.name)
dog.eat()
mouse.sleep()
dog.speak()