score=0
guesses=[]
questions=["what is the capital of pakistan ?",
           "where most pyramids in the world are located ?",
           "what is the capital of india ?",
           "who won the 2022 FIFA world cup ?",
           "which loop is used in python to iterate over a sequence of numbers ?",]
options=[["a. karachi","b. islamabad","c. lahore","d. peshawar"],
         ["a. egypt","b. mexico","c. peru","d. italy"],
            ["a. delhi","b. mumbai","c. kolkata","d. chennai"],
            ["a. argentina","b. france","c. germany","d. brazil"],
            ["a. for loop","b. while loop","c. do-while loop","d. foreach loop"]]
answers=["b","a","a","a","a"]
while True:
    for i in range(len(questions)):
        question = questions[i]
        print(question)
        for option in options[i]:
            print(option)
        guess=input("chosee your option ??")
        guesses.append(guess)
        if guess==answers[i]:
            print(" correct !")
            score+=1
        else:
            print(" wrong !")
        print(f" your score is {score}/5")
    break
print("quiz completed")
print("")
print("correct answers are :")
for answer in answers:
    print(f" {answer}",end=" ")
print("")
print("your guesses are :")
for guess in guesses:
    print(f" {guess}",end=" ")