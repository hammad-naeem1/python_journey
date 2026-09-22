import random
expense=[]
amount=[]
total_expense=0
while True:
    print('''1. Add Expense
2. View All Expenses
3. View Total Spending
4. remove an expense
5. Exit''')
    option=input("chosee a option !")
    if option=="1":
        name=input(" enter expense name ! ")
        while True:
            try:
                amountt=int(input(" enter expense amount ! "))
                total_expense=total_expense+amountt
            except ValueError:
                print("  enter a number")
            else:break
        expense.append(name)
        amount.append(amountt)
        print(" expense added !")
    elif option=="2":
        if not expense:
            print(" no expense ! stored yet !")
        else:
            for x in expense :
                for i in amount:           
                 print(f"item {expense}:amount {amount}")
    elif option=="3":
        if total_expense<=0:
            print(" no expense ! stored yet ")
        else:
            print(f" your total amount is ${total_expense}")
    elif option=="4":
        pass
    elif option=="5":
        print(" thanks for using our program : ")
        exit()
    else:
        print(" please enter a valid option :")