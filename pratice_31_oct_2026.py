class computer_store:
    def stock(self):
        return " full stock avalible "


class laptop(computer_store):
    def __init__(self,price,model,brand):
        self.price=price
        self. model=model
        self.brand=brand


class mobile(computer_store):
    def __init__(self,price,model,brand):
         self.price=price
         self. model=model
         self.brand=brand

laptop=laptop(price='7000$',model='2026',brand='macbook')
mobile=mobile(price='5000$',model='2021',brand='iphone')
while True:
    choice=input('''what you want sir ? q to exit 
(laptop__ price , model , brand ,stock ?)
(mobile__ price , model , brand ,stock      ?)
''').lower()
    if choice=="laptop price":
        print(laptop.price)
    elif choice=="laptop model":
        print(laptop.model)
    elif choice=="laptop brand":
        print(laptop.brand)
    elif choice=="laptop stock":
        print(laptop.stock())
    elif choice=="mobile price":
            print(mobile.price)
    elif choice=="mobile model":
            print(mobile.model)
    elif choice=="mobile brand":
            print(mobile.brand)
    elif choice=="mobile stock":
            print(mobile.stock())
    elif choice=="q":
         print(' thanks for visiting !')
         break
    else:
         print(' enter a valid option')


