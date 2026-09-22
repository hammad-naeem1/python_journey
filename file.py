while True:
    try:
        name=int(input(" what is your num !!"))
        with open("file.io.txt","a") as file:
                file.write(f"{name}\n")
    except ValueError:
         continue
    else:     
     break


# name=input(" what is your name ?!!")
# with open("file.txt","a") as file:
#     file.write(f"{name}\n")

with open("file.io.txt") as file:

    for line in sorted(file):

        print(f"hello {line}", end="")
