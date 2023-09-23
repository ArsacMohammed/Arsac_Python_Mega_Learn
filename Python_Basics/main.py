
#storing the list in the text files.
while True:
    user_actions= input ("Type add ,edit ,show ,complete or exit ").strip()

    match user_actions:
        case "add":
            with open("todo.txt","r") as file:
                todos = file.readlines()

            todo= input ("Enter a todo: ")+"\n"
            todos.append(todo)

            with open("todo.txt", "w") as file:
                file.writelines(todos)
        case "show":
            with open("todo.txt","r") as file:
                todos = file.readlines()

            for index ,todo in enumerate (todos):
                todo=todo.strip("\n")
                todo = todo.title()
                print(f"{index + 1}-{todo}")
        case "edit":
            number = int(input ("enter the number of the todos to edit :  "))
            edited_todo= input ("enter the todo for the new todo: ")
            todos[number-1]=edited_todo
        case "complete":
            number = int(input ("which one do you wanna remove , number only"))
            todos.pop(number -1 )
        case "exit":
            break
print("bye")


