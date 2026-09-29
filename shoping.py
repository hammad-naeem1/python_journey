products = {
    "laptop": {"price": 75, "stock": 10},
    "phone": {"price": 30, "stock": 8},
    "computer": {"price": 120, "stock": 5},
    "playstation": {"price": 400, "stock": 3},
    "earphone": {"price": 20, "stock": 15}
}
list=[]



store=print('''t=========================
      MY STORE
========================

1. View Products
2. Add to Cart
3. Remove from Cart
4. View Cart
5. Checkout
6. Exit''')
while True:
    option=input(" enter your option : (q to exit )")
    if option=="q":
        break
    elif option=="1":
     print("\n===== PRODUCTS =====")
     for product, details in products.items():
        print(f"{product.title():12} ${details['price']:>4}   Stock: {details['stock']}")
    elif option=="2":
       buy=input(" what you want sir :?")
       list.append(buy)
    if buy==
       
