class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print("my name is",self.name,"and my age is",self.age)
student1=student("hammad",20)
student2=student("ali",21)
student1.introduce()
student2.introduce()