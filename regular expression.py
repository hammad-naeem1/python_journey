import re 

email=input(" what is your email ").strip()

if re.search(r".+@.+\.com$", email):
    print("valid")
else:
    print(" invalid")
