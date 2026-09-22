class city:
    def __init__(self,town,village):
        self.town=town
        self.village=village
    def office(self):
           print(f"there is offises in {self.village} ")
    
    
class town(city):
    def people(self):
            print(f"there is people in {self.village}:{self.town} ")
class village(city):
     def shop(self):
             print(f"there is  shops in   {self.village}:{self.town}")

village=village('mianaz','alandoor')
town=town('mianaz','alandoor')

village.shop()
town.people()
town.office()