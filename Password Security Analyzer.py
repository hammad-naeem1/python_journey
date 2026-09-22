length=0
upper=0
lower=0
digit=0
others=0
while True:
    password=input("Enter your password: (q to quit) ")
    if password == 'q':
        print("Thanks for using the program...")
        break
    for i in range(len(password)):
        length+=1
    print(f"The length of the password is: {length}")
    print("")
    for uppercase in password:
        if uppercase.isupper():
            upper+=1
    print(f"The number of uppercase letters in the password is: {upper}")
    print("")  
    for lowercase in password:
        if lowercase.islower():
            lower+=1
    print(f"The number of lowercase letters in the password is: {lower}")
    print("")
    for digits in password:
        if digits.isdigit():
            digit+=1
    print(f"The number of digits in the password is: {digit}")
    print("")
    for other in password:
        if not other.isalnum():
            others+=1
    print(f"The number of special characters in the password is: {others}")
    if lower < 3 or upper < 3 or digit < 2 or length < 8:
        print("")
        print("Password is weak!")
    else:
       print("")
       print("Password is strong!")

