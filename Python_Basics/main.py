

while True:
    user_actions= input ("Type add ,edit ,show ,complete or exit ").strip()

# this program will produce an error if the input for the user_actions is edit add a new member , here the add will get executed
# to avoid this we use startswith function.
    if user_actions.startswith("add"):
        with open("todo.txt","r") as file:
            todos = file.readlines()

        todo= user_actions[4:]+"\n"
        todos.append(todo)

        with open("todo.txt", "w") as file:
            file.writelines(todos)
    elif user_actions.startswith("show"):
        with open("todo.txt","r") as file:
            todos = file.readlines()

        for index ,todo in enumerate (todos):
            todo=todo.strip("\n")
            todo = todo.title()
            print(f"{index + 1}-{todo}")
    elif user_actions.startswith("edit") :
        try:
            number =int( user_actions[5:])

            with open("todo.txt","r") as file:
                todos = file.readlines()
            edited_todo = input("enter the todo for the new todo: ") +"\n"
            todos[number - 1] = edited_todo
            with open("todo.txt","w") as file:
                file.writelines(todos)
        except ValueError:
            print("your command is not valid ")
            continue
    elif user_actions.startswith("complete"):
        try:
            number = int (user_actions[9:])
            with open("todo.txt","r") as file:
                todos = file.readlines()
            todos.pop(number -1 )

            with open("todo.txt","w") as file:
                file.writelines(todos)
        except IndexError:
            print("There is no element with that number .")
            continue
        except ValueError:
            print("Your command is not valid ..")

    elif user_actions.startswith("exit"):
        break

    else:
        print("Invalid command ... Try Again ")
print("bye")


