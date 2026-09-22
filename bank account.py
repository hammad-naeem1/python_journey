print('''         
         ================================ 
         WELCOME TO THE OUR BANK 
         ================================                 
''') 

balance = 5000 
attempt = 3 

name = input("what is your good name?__") 


while True: 
    try: 
        for i in range(attempt): 

            pin = int(input("what's your pin?_")) 

            if pin == 1990: 
                print("login successful, Welcome!")

                # ❌ MISTAKE 1:
                # You printed successful, but you didn't break the FOR loop.
                # So Python continues asking for the PIN.
                 
            else: 
                print("kindly enter correct pin") 

        print("you have reached limit: account blocked!!")

        # ❌ MISTAKE 2:
        # This ALWAYS runs after the for loop finishes.
        # Even if the correct PIN was entered.
        
        pass 

    except ValueError: 
        print("please enter an int or a number") 

    else: 
        break 


transition_history = 0 

print('''         
         ================================ 
                    MENU 
         ================================                 
''') 

costumer = input('''what you want sir?? 
1, deposit 
2, withdraw 
3, check_balance 
4, exit
''') 


if costumer == "1": 

    deposit = int(input("how much you wanna deposit sir?")) 

    if deposit >= 1: 
        print("here is your new balance sir!!", balance + deposit) 

        # ❌ MISTAKE 3:
        # This calculates and PRINTS the new balance,
        # but it does NOT actually change balance.
        #
        # You need:
        # balance = balance + deposit

        transition_history = transition_history + 1 

    # elif deposit <= 1:
    #    print("can't add minus number sorry!!")

    # ❌ MISTAKE 4:
    # You commented this out.
    # Therefore, if the deposit is 0 or negative,
    # the program simply does nothing.
    #
    # You need an ELSE here.


elif costumer == "2": 

    withdraw = int(input("how much you wanna withdraw sir?")) 

    if withdraw <= balance: 

        print("here is your new balance sir!!", balance - withdraw) 

        # ❌ MISTAKE 5:
        # Same problem as deposit.
        # You're only PRINTING the new balance.
        # You're not changing balance.
        #
        # You need:
        # balance = balance - withdraw

        transition_history = transition_history + 1 

    elif withdraw >= balance: 
        print("insufficient Balance")

        # ⚠️ MISTAKE 6:
        # If withdraw == balance, this condition also becomes true:
        #
        # withdraw <= balance
        #
        # So the withdrawal is actually allowed.
        #
        # That's not necessarily wrong!
        # Withdrawing your entire balance can be allowed.
        #
        # But if you want to prevent it, use the condition you actually want.


elif costumer == "3": 

    print("here is your balance sir ", balance) 


elif costumer == "4": 

    print("thanks for using our Bank!!") 
    exit() 


else: 
    print("kindly enter a valid option") 


print(f''' 
name__{name}  
transition history {transition_history} time 

================================ 
      Thanks for using our Bank 
================================                                        
please come AGAIN!!!
''')