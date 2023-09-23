
#storing the list in the text files.
while True:
    user_actions= input ("Type add ,edit ,show ,complete or exit ").strip()

    match user_actions:
        case "add":
            file=open("todo.txt","r")
            todos=file.readlines()
            file.close()  # the above three lines move the cursor to the end of the text files and write funciton in below code will worte the input string to the text ,otherwise the text file will get overrideen by the new input and previous are all lost .
            todo= input ("Enter a todo: ")+"\n"
            todos.append(todo)
            file=open("todo.txt","w")
            file.writelines(todos)
            file.close()  # these are important prevent resource leakage.
        case "show":
            file = open("todo.txt","r")
            todos= file.readlines()
            file.close()
            for index ,todo in enumerate (todos):
                todo = todo.title()
                print(f"{index + 1}-{todo}")
                #this is the output and has  extra line space vbecause the print provide its own linedpace.
                # 1 - Clean
                #
                # 2 - Wipe
                #
                # 3 - Shower
                #
                # 4 - Move
                #
                # 5 - Prepare

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


