todos=[]
while True:
    user_actions= input ("Type add ,edit ,show or exit ").strip()

    match user_actions:
        case "add":
            todo= input ("Enter a todo: ")
            todos.append(todo)
        case "show":
            for todo in todos:
                todo = todo.title()
                print(todo)

        case "edit":
            number = int(input ("enter the number of the todos to edit :  "))
            edited_todo= input ("enter the todo for the new todo: ")
            todos[number-1]=edited_todo
        case "exit":
            break
print("bye")
