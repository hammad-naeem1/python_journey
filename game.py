import random
Player_hp=100
enemy_hp=100
print('''
------------------------------------------------------------
        WELCOME TO THE GAME OF DEATH  
------------------------------------------------------------''')
while True:
    if Player_hp<=0:
      print(" computer wins !  ")
      break
    elif enemy_hp<=0:
        print(" you won !")
        break
    else:
       while True :
            try:
              choice=int(input(''' 
        chosee  a option :
                        1,normal_
                        2,hard,__
                        3,heal __ ''' ))
            except ValueError:
               print("please type a integar ")
            else:
               break
    while True:
       if choice==1:
             toss=input("press 1 to attack first  and 2 to let computer attack  :")
             if toss=="1":
                    while True:
                                player=input("  you prees 1 to attack ")
                                if player=="1":
                                    a=10
                                    b=20
                                    c=random.randint(a,b)
                                    enemy_hp=enemy_hp-c
                                    print(" you attacked !")
                                    print("computer hp remaing _",enemy_hp)
                                    print("")
                                    print(" computer turn !")
                                    print("computer attacked !")
                                    a=10
                                    b=20
                                    c=random.randint(a,b)
                                    Player_hp=Player_hp-c
                                    print("your hp remaing _",Player_hp)
                                elif Player_hp<=0:
                                    print(" computer wins !  ")
                                    break
                                elif enemy_hp<=0:
                                    print(" you won !")
                                    break 
                                else:
                                    ("please enter a valid attack option")
             elif toss=="2":
                  print("computer attacked !")
                  a=10
                  b=20
                  c=random.randint(a,b)
                  Player_hp=Player_hp-c
                  print("your hp remaing _",Player_hp)
                  player=input("  you prees 1 to attack ")
                  if player=="1":
                     a=10
                     b=20
                     c=random.randint(a,b)
                     enemy_hp=enemy_hp-c
                     print(" you attacked !")
                     print("computer hp remaing _",enemy_hp)  
                     print("your hp remaing _",Player_hp)
                  elif Player_hp<=0:
                   print(" computer wins !  ")
                   break
                  elif enemy_hp<=0:
                   print(" you won !")
                  break 

             else:
                 print(" select a valid option :")
    
       elif choice==2:
           toss=input("press 1 to attack first  and 2 to let computer attack  :")
           if toss=="1":
                               while True:
                                           player=input("  you prees 1 to attack ")
                                           if player=="1":
                                               a=30
                                               b=50
                                               c=random.randint(a,b)
                                               enemy_hp=enemy_hp-c
                                               print(" you attacked !")
                                               print("computer hp remaing _",enemy_hp)
                                               print("")
                                               print(" computer turn !")
                                               print("computer attacked !")
                                               a=30
                                               b=50
                                               c=random.randint(a,b)
                                               Player_hp=Player_hp-c
                                               print("your hp remaing _",Player_hp)
                                           elif Player_hp<=0:
                                            print(" computer wins !  ")
                                            break
                                           elif enemy_hp<=0:
                                            print(" you won !")
                                            break   
                                           else:
                                               print("please enter a valid attack option")
           elif toss=="2":
                             print("computer attacked !")
                             a=30
                             b=50
                             c=random.randint(a,b)
                             Player_hp=Player_hp-c
                             print("your hp remaing _",Player_hp)
                             player=input("  you prees 1 to attack ")
                             if player=="1":
                                a=30
                                b=50
                                c=random.randint(a,b)
                                enemy_hp=enemy_hp-c
                                print(" you attacked !")
                                print("computer hp remaing _",enemy_hp)  
                             elif Player_hp<=0:
                              print(" computer wins !  ")
                              break
                             elif enemy_hp<=0:
                              print(" you won !")
                              break   
                             else:
                                  print(" enter a  valid option")

       elif choice==3:
              if Player_hp >90:
                    print("soory ! sir healing is not avalable your hp is above 90")
                    break
              elif Player_hp <90:
               a=1
               b=10
               c=random.randint(a,b)
               Player_hp=Player_hp+c
               print(f"you healed yourself_{c}points_your hp is_{Player_hp}")
              break
    
                    
                        
                                 
                        