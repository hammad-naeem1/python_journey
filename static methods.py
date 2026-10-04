# ======
# statics method
# ===
# a method that belongs to a class rather than  any object from that class (instance)
# # usally used for  gerenal utality functions

# instance method= best for operatins on instances of the class  (objects)
# static method =best for utality  funcrtons that do not nedd acess to class data

class employee:


    def __init__(self,name,positon):
        self.name=name
        self.positon=positon

    def get_info(self):
        return f"{self.name}={self.positon}"
    # this is a instance_method 
p
    @staticmethod
    def is_valid_position(position):
        valid_position=["manager","cashier",'boss','watchman']
        return position in valid_position
        # this is a staticmethod


employe1=employee('hammad','boss')
employe2=employee('barahjan','watchman')
print(employe1.get_info())

print(employee.is_valid_position('boss'))
