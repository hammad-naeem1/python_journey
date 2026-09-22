if choice==1:
          print("computer attacked !")
          a=10
          b=20
          c=random.randint(a,b)
          Player_hp=Player_hp-c
          print("your hp remaing _",Player_hp)
          while True:
            player=input("  you prees 1 to attack ")
            if player=="1":
                a=10
                b=20
                c=random.randint(a,b)
                enemy_hp=enemy_hp-c
                print("computer hp remaing _",enemy_hp)
                break
            else:
                ("please enter a valid attack option")
    elif choice==2:
                  print("computer attacked !")
                  a=30
                  b=50
                  c=random.randint(a,b)
                  Player_hp=Player_hp-c
                  print("your hp remaing _",Player_hp)
                  while True:
                    player=input("   prees 1 to attack ")
                    if player=="1":
                        a=30
                        b=50
                        c=random.randint(a,b)
                        enemy_hp=enemy_hp-c
                        print("computer hp remaing _",enemy_hp)
                        break
                    else:
                        ("please enter a valid attack option")
    elif choice==3:
           if Player_hp >90:
               print("soory ! sir healing is not avalable your hp is above 90")
           elif Player_hp <90:
                a=1
                b=10
                c=random.randint(a,b)
                Player_hp=Player_hp+c
                print(f"you healed yourself_{c}points_your hp is_{Player_hp}")
   



                    



print("computer hp remaing _",enemy_hp)
                          print(" its time for computer !")
                          print("computer attacked !")
                          a=10
                          b=20
                          c=random.randint(a,b)
                          Player_hp=Player_hp-c
                          print("your hp remaing _",Player_hp)  

















 elif  toss=="2" and choice==1:
            print("computer attacked !")
            a=10
            b=20
            c=random.randint(a,b)
            Player_hp=Player_hp-c
            print("your hp remaing _",Player_hp)  
        if toss=="1" and choice==2:
                    while True:
                                player=input("  you prees 1 to attack ")
                                if player=="1":
                                 a=30
                                 b=50
                                c=random.randint(a,b)
                                enemy_hp=enemy_hp-c
                                print("computer hp remaing _",enemy_hp)
                                break

        elif  toss=="2" and choice==2:
                    print("computer attacked !")
                    a=30
                    b=50
                    c=random.randint(a,b)
                    Player_hp=Player_hp-c
                    print("your hp remaing _",Player_hp)
        elif toss=="3" and choice==3:
               if Player_hp >90:
                   print("soory ! sir healing is not avalable your hp is above 90")
               elif Player_hp <90:
                    a=1
                    b=10
                    c=random.randint(a,b)
                    Player_hp=Player_hp+c
                    print(f"you healed yourself_{c}points_your hp is_{Player_hp}")
       
           
          

           toss=input("press 1 to attack first  and 2 to let computer attack  :")