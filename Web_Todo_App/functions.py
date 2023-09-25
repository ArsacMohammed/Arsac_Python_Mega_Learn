FilePath="todo.txt"


import os

def get_todo():
    with open(FilePath, "r") as file:
        todos = file.readlines()
        return todos
def write_todos(todos):
    with open(FilePath, "w") as file:
        file.writelines(todos)
