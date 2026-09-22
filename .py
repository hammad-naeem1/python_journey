
import statistics
import random

tasks = []
completed_tasks = []

while True:
    option = input('''1. Add task
2. Show tasks
3. Complete task
4. Random task
5. Statistics
6. Exit
__''')

    if option == "1":
        while True:
            player = input("what is your task? (q for exit) ")

            if player == "q":
                break
            else:
                tasks.append([player])

    elif option == "2":
        if len(tasks) == 0:
            print("no tasks in record")
        else:
            for x in tasks:
                for z in x:
                    print(z)

    elif option == "3":
        while True:

            if len(tasks) == 0:
                print("no tasks in record")
                break

            else:
                for x in range(len(tasks)):
                    print(x + 1, tasks[x][0])

                user = input("choose the number you want to remove (q to exit): ")

                if user == "q":
                    break

                try:
                    user = int(user)

                    if user < 1 or user > len(tasks):
                        print("please choose a valid task number")
                        continue

                    removed_task = tasks.pop(user - 1)
                    completed_tasks.append(removed_task)

                    print("task completed!")

                except ValueError:
                    print("please enter a number")

                else:
                    break

    elif option == "4":
        if len(tasks) == 0:
            print("no tasks in record")
        else:
            random_task = random.choice(tasks)
            print(random_task[0])

    elif option == "5":
        print(f'''
total task: {len(tasks) + len(completed_tasks)}
completed task: {len(completed_tasks)}
remaining task: {len(tasks)}
''')

    elif option == "6":
        print(" thanks for using our program !")
        break

    else:
        print("please enter a valid option")
