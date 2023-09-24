import PySimpleGUI as sg
label=sg.Text("Type in a todo")
inputText = sg.InputText("Enter todo")
add_Button =sg.Button("Add")
window = sg.Window("My_App_Todo",layout=[[label],[inputText,add_Button]])
window.read()
window.close()



#to install pysimplewindow go to setting - click under your project name - click interpretor - install by type name of the module - install