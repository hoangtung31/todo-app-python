import streamlit as st
import functions

st.title("My To-do App")
st.subheader("This is my todo app")
st.write("This app is to increase you app productivity.")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input("")