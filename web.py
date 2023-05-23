import streamlit as st
import functions

st.title("My To-do App")
st.subheader("This is my todo app")
st.write("This app is to increase you app productivity.")

todos = functions.get_todos()


def get_todo():
    entered_todo = st.session_state["new_todo"] + "\n"
    todos.append(entered_todo)
    functions.write_todos(todos)


for todo in todos:
    st.checkbox(todo)

st.text_input(label="hello", placeholder="Enter new todo....", on_change=get_todo, key='new_todo')
st.session_state
