#To-Do App
tasks = []

while True:
    select = input("Choose your action (add, view, delete, exit): ").lower()
    if select == "add":
        task = input("Enter your task: ").lower()
        tasks.append(task.lower())
        print(f"{task.title()} added.")
    elif select == "view":
        if tasks:
            for item in tasks:
                print(item.title())
        else:
            print("Nothing is in the task.")
    elif select == "remove":
        task = input("Enter the name of the task: ").lower()
        if task in tasks:
            tasks.remove(task.lower())
            print(f"{task.title()} removed")
        else:
            print("Task is not in found.")
    elif select == "exit":
        print("You leave the to do task.")
        break
    else:
        print("Invalid character, try again.")