import streamlit as st
import functions

st.title("Todo App")
st.subheader("This Todo App will increase your productivity")
st.write("Things to do ")
todos = functions.get_todo()


def add_todo():
    todo_to_add = st.session_state["new_todo"] +"\n"
    todos.append(todo_to_add )
    functions.write_todos(todos)


for index,todo in enumerate(todos):
    check=st.checkbox(todo,key=todo)
    if (check):
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo ", placeholder="Add a todo ", on_change=add_todo, key="new_todo")
print("hello")
