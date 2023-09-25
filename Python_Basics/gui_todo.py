import PySimpleGUI as sg
import functions
import time


clock=sg.Text("",key="clock")
sg.theme("Black")
label = sg.Text("Type in a todo")
inputText = sg.InputText("Enter todo", key="todo")
add_Button = sg.Button("Add")
edit_button = sg.Button("Edit", size=(3, 1))
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
listbox = sg.Listbox(functions.get_todo(), key="todos", enable_events=True, size=(43, 10))
layout = [[clock],[label], [inputText, add_Button], [listbox, edit_button,complete_button],[exit_button]]
window = sg.Window("My_App_Todo", layout=layout)

while True:

    event, values = window.read(timeout=300)
    window["clock"].update(time.strftime("%b %d ,%Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values["todo"] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_edit = values["todos"][0]
                todos = functions.get_todo()
                index_to_edit = todos.index(todo_edit)
                todos[index_to_edit] = values["todo"] + "\n"
                functions.write_todos(todos)
                # this windows["todos"] create an instance of the listbox through windows .
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("There is no element selected... please select one   ")

            # to print the list  in the list box in the gui ,use input text instance by "todo" key
        case "todos":
            try:
                window["todo"].update(value=values["todos"][0])
            except IndexError:
                sg.popup("There is no list item present ")

        case "Complete":
            try:
                todo_remove=values["todos"][0]
                todos=functions.get_todo()
                todos.remove(todo_remove)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("There is no element selected... please select one")

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
