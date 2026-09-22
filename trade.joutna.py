pair=[]
direction=[]
profit_or_loss=[]
print("===== TRADING SESSION ====")
while True:
            try:
                initial_balance=int(input(" what is yout intaial_balance __"))

            except ValueError:
                print(" enter a integar !")
            else:
                break
while True:
    option = input('''1. Add Trade
2. Show trades
3. show / loss
4. Exit
__''')
    if option=="1":
        choice_trade=input(" Enter your Pair !")
        choice_trade2=input(" trade direction !")
        while True:
            try:
                choice_trade3=int(input(" Enter your profit or loss on trade !"))

            except ValueError:
                print(" enter a integar !")
            else:
                break
        pair.append(choice_trade)
        direction.append(choice_trade2)
        profit_or_loss.append(choice_trade3)
    elif option=="2":
        if not pair:
            print("no data found in system !")
       
        else:
            for pairs, directions, pnl in zip(pair, direction, profit_or_loss):
                print(f"--- TRADE ----")
                print(f"{pairs} || {directions} || PNL = ${pnl}")
    elif option=="3":
        pnl=sum(profit_or_loss)
        print(f" your  today pnl is _${pnl}")
        initial_balance=initial_balance + pnl
        print(f" now your balance is _${initial_balance}")
    elif option=="4":
        print(" thanks for checking out our program")
        exit()
    else:
       print(" please enter a valid option !")

