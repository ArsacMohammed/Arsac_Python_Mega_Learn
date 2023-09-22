todos=[]
while True:
    user_actions= input ("Type add ,edit ,show ,complete or exit ").strip()
#now adding enumerate function for the for loop
    match user_actions:
        case "add":
            todo= input ("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index ,todo in enumerate (todos):
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


# 0 - Clean
# 1 - Throw
# 2 - Move   these are the output and have spaces even though is not given in the code.fstring can solve that problem.
