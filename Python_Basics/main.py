

while True:
    user_actions= input ("Type add ,edit ,show ,complete or exit ").strip()


    if "add" in  user_actions:
        with open("todo.txt","r") as file:
            todos = file.readlines()

        todo= user_actions[4:]+"\n"
        todos.append(todo)

        with open("todo.txt", "w") as file:
            file.writelines(todos)
    elif "show" in user_actions:
        with open("todo.txt","r") as file:
            todos = file.readlines()

        for index ,todo in enumerate (todos):
            todo=todo.strip("\n")
            todo = todo.title()
            print(f"{index + 1}-{todo}")
    elif "edit" in user_actions :
        number =int( user_actions[5:])

        with open("todo.txt","r") as file:
            todos = file.readlines()
        edited_todo = input("enter the todo for the new todo: ") +"\n"
        todos[number - 1] = edited_todo
        with open("todo.txt","w") as file:
            file.writelines(todos)

    elif "complete"  in user_actions:
        number = int (user_actions[9:])
        with open("todo.txt","r") as file:
            todos = file.readlines()
        todos.pop(number -1 )

        with open("todo.txt","w") as file:
            file.writelines(todos)


    elif "exit" in user_actions:
        break

    else:
        print("Invalid command ... Try Again ")
print("bye")


