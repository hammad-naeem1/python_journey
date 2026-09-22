# simply the loop inside a loop is nested loop
    # eg ⬇️⬇️

rows=int(input(" enter the num of the raw__"))
symbol=input(" enter the symbol__")
coloums=int(input(" enter the num of the coloums__"))
for i in range(rows):
    for x in range(coloums):
        print(symbol, end="")
    print()
