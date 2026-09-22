
while True :    
  option=input(' prees c too countinue and q to quit:')
  if option=="c":
    while True:
            try:
                bill=int(input(f"what's the bill amount : "))
                tip_percentage=int(input(f" how much tip you want to leave : "))
                people_spillting=int(input(f"how many people your spliting bill with : ?"))
            except ValueError:
                print(' enter a num kindly :')
            else:
                break
    total=bill+tip_percentage
    each_person=bill/people_spillting
    print(f'''
sir your total would be {total}
each person would pay   {each_person}
''')
  elif option=="q":
      print(' thansks for using our program  ')
      break
  else:
      print('enter a valid option')