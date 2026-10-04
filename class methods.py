# =====
# class mwthods
# =======
            # allow operation to class itself
            # take (clas)as a first parametre ,which represt the class itself 


class studnet:
    count=0
    total_gpa=0

    def __init__(self,name, gpa ):  
        self. name=name
        self. gpa=gpa
        studnet.count+=1
        studnet.total_gpa+=gpa

    # this is an instance method 
    def get_info(self):
        return f" {self.name} : {self.gpa}"



    # this is a class method 

    @classmethod

    def get_count(cls):
        return f"total of the students : {cls.count:.2f}"
    @classmethod
    def average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"




studnet1=studnet("ali", 3.5)
studnet2=studnet(' hammad',4)



print(studnet1.get_info())
print(studnet2.get_info())
print(f" avg gpa :{studnet.average_gpa()}")
print(f"total studensts: {studnet.get_count()}")

    