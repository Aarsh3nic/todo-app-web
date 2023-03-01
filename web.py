import streamlit as st
import functions

label = ""


def add_todo():
    todo = st.session_state["new_todo"] + "\n"

    if todo in todos:
        st.session_state["new_todo"] = "Todo already exists!,Please enter a different one"

    elif todo.strip("\n") == "":
        st.session_state["new_todo"] = "Enter a value first"

    else:
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


todos = functions.get_todos()

st.title("My Todo App")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="Enter task:",placeholder="Add a new todo:",
              on_change=add_todo, key="new_todo" ,label_visibility="hidden")
