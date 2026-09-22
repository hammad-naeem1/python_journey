my_list=[]
while True:
    try:
        for x in range(5):
            element=int(input(" write your numbers__ "))
            my_list.append(element)
    except ValueError:
        print(" please enter a number")
        continue
    else:
        break
print(f" so your numbers are ::{my_list}",end="")

for i in my_list %2:
    print(my_list)
