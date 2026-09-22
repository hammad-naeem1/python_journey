expense=[]
expenses=0

print('''1. Add Expense
2. View Expenses
3. Total Spent
4. Find Most Expensive
5. Delete Expense
6. Exit''')
while True:
    option=input("Enter your option:  (q to exit)")
    if option=="q":
        break
    elif option=="1":
        input_expense=input("Enter the expense amount: ")
        expense.append(input_expense)
    elif option=="2":
       for x in range(len(expense)):
            if expense[x]>0:
                print(f"{[x]}")
            elif expense<0:
                print(f"expenses :: {expense[x]}")
    elif option=="3":
        expenses=expense=+expense
        if expense>0:
            print(" sorry no record ")
        elif expense<0:
            print(expenses)
    