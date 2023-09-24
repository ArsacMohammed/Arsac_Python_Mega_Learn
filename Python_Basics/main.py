import functions

while True:
    user_actions = input("Type add ,edit ,show ,complete or exit ").strip()

    # this program will produce an error if the input for the user_actions is edit add a new member , here the add will get executed
    # to avoid this we use startswith function.
    if user_actions.startswith("add"):

        todo = user_actions[4:] + "\n"
        todos = functions.get_todo()
        todos.append(todo)
        functions.write_todos(todos)


    elif user_actions.startswith("show"):
        todos = functions.get_todo()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            todo = todo.title()
            print(f"{index + 1}-{todo}")



    elif user_actions.startswith("edit"):
        try:
            number = int(user_actions[5:])

            todos = functions.get_todo()
            edited_todo = input("enter the todo for the new todo: ") + "\n"
            todos[number - 1] = edited_todo
            functions.write_todos(todos)
        except ValueError:
            print("your command is not valid ")
            continue



    elif user_actions.startswith("complete"):
        try:
            number = int(user_actions[9:])
            todos = functions.get_todo()
            todos.pop(number - 1)

            functions.write_todos(todos)
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
### command line code for todo program is done moving to build the graphical user interface.
