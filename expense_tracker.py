import statistics
expenses = []
amounts = []
categories = []
total_expense=0
print('''
=====================================================
               Expense Tracker
===================================================''')

while True:
    option=input('''
1,Add Expense
2,Show All Expenses
3,Search Expenses
4,Show Statistics
5,Show Categories
6,Delete Expense
7,Exit
Enter your choice:''')
    if option=="1":
      input_expense=input(" enter the expense name  !")
      input_categorie=input(" input the cetogary    !")
      while True:
                 try:
                          while True :
                             input_amount=int(input("enter the amount !"))
                             total_expense=total_expense+input_amount
                             if input_amount<=0:
                                   print(" enter valid amount")
                             else:
                                   break
                                
                 except ValueError:
                        print(" enter a valid amount !")
                 else:
                        break 
      expenses.append(input_expense)
      amounts.append(input_amount)
      categories.append(input_categorie)
    elif option=="2":
           if not expenses:
                  print(" no record found !")
           else:
                ultimate_expense=zip(expenses,amounts,categories)
                for input_expense,input_amount,input_categorie in ultimate_expense:
                       print(f" your_item |{input_expense}|amount|{input_amount}|cetogary|{input_categorie}")
    elif option=="3":
          search=input(" enter your expense _")
          if search not in expenses:
                print("  expense not found")
          elif search in expenses:
                index=expenses.index(search)
                print(f'''
item founded
your item |{expenses[index]}|amount|{amounts[index]}|cetogary|{categories[index]}''')
    
    elif option=="4":
          if not expenses:
                print(" no record ")
          else:
            w=statistics.mean(amounts)
            a=min(amounts)
            b=max(amounts)
            print(f''' your total expense amount is {total_expense}
your maxium expense amount is {b}
your lowest expense amount is {a}
your average expense amount is {w}
''')
    elif option=="5":
              if not expenses:
                    print(" no record")
              else:
                ultimate_cetogary=zip(expenses,categories)
                for input_expense,input_categoriy in ultimate_cetogary:
                        print(f" your expense __{input_expense} | your cetogary|{input_categorie}")
    elif option=="6":
          delete=input(" enter your expense to delete !")
          if delete not in expenses:
                print(f"{delete}-not found !")
          elif delete in expenses:
                index=expenses.index(delete)
                expenses.pop(index)
                amounts.pop(index)
                categories.pop(index)
                print(f"{delete} remove sucessfully! ")
    elif option=="7":
          print(" thanks for using our program !")
          exit()
    else:
          print(" enter a valid option ")
          