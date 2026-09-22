print(" welcome sir ")
name=input(" what is your name sir ?? ::")
password="python123"
guess=""
while guess!=password:
    guess=input(" please enter your password::")
    if guess==password:
        print(" correct password welcome !! MR",name)
    else:
        print(" please enter the correct password sir ::")






# print("Welcome Sir!")

# name = input("What is your name? ")

# password = "python123"
# guess = ""
# attempts = 0

# while guess != password and attempts < 3:

#     guess = input("Please enter your password: ")
#     attempts = attempts + 1

#     if guess == password:
#         print("✅ Welcome Mr.", name)
#         print("Login successful!")
#     else:
#         print("❌ Wrong password.")
#         print("Attempts:", attempts)

# if attempts == 3 and guess != password:
#     print("🔒 Account Locked!")


