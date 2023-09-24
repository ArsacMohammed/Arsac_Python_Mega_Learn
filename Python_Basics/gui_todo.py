import PySimpleGUI as sg
import functions

label = sg.Text("Type in a todo")
inputText = sg.InputText("Enter todo", key="todo")
add_Button = sg.Button("Add")
edit_button = sg.Button("edit", size=(3, 1))
complete_button = sg.Button("complete")

listbox = sg.Listbox(functions.get_todo(), key="todos", enable_events=True, size=(43, 10))
layout = [[label], [inputText, add_Button], [listbox, edit_button]]
window = sg.Window("My_App_Todo", layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values["todo"]
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "edit":
            todo_edit = values["todos"][0]
            todos = functions.get_todo()
            index_to_edit = todos.index(todo_edit)
            todos[index_to_edit] = values["todo"] + "\n"
            functions.write_todos(todos)
            # this windows["todos"] create an instance of the listbox through windows .
            window["todos"].update(values=todos)

            # to print the list  in the list box in the gui ,use input text instance by "todo" key
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()
