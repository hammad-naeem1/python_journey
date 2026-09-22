print(" welcome to the super market🍎🍌🍊 ")
name=input(" what is your name sir??__")
products={                                            
        "apple": 150,
        "grape": 175,
        "mango": 200,
        "orange": 125,
        "lemon": 300                                         
}
for i in products:
    print(i,products[i],       sep="__")
user_input=""
while True:
    user_input=input(" what you want sir??__")
    if user_input in products:
        quantity=int(input(" how much u want to buy sir??__"))
        break
    else :
        print(" chosee something which is in menu!!!")
price = products[user_input]
total = price * quantity

q=print(f'''Here is your bill__ {total}
here are our payment options sir : card // cash  ?''')
while True :
    card_payment=input(" enter a payment please!!__")
    if card_payment=="card":
        print("  ok ! card would be perfect")
        break
    elif card_payment=="cash":
        print(" ok ! cash would be perfect")
        break
    else:
        print(" please enter something valid__")
print(f'''         Here Is Your Recipt SIR!!   
costumer__{name}
product__{user_input}
quantity__{quantity}
total__{total}
payment__{card_payment}
THANKS FOR SHOPPING SIR!!''')

