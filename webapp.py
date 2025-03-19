import streamlit as st
import functions

st.title("My Todo App")
st.write("This app is to increase your productivity")

todos = functions.get_todos()

def add_todo():
  todo = st.session_state["new_todo"].strip()
  todos.append(todo + "\n")
  functions.write_todos(todos)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key = "new_todo")

for index, todo in enumerate(todos):
  checkbox = st.checkbox(todo, key=todo)
  if checkbox:
    todos.pop(index)
    functions.write_todos(todos)
    del st.session_state[todo]
    st.rerun()

