class laptop:
    def __init__(self, charger ,screen,company  ):
        self.charger=charger
        self.screen=screen
        self.company=company
    def laptop_specs(self):
        print(f"charger :{self.charger  } : {self.screen}  : company : {self.company} ")
laptop1=laptop(' 45w ','samsung screen','dell')
laptop1.laptop_specs()