import functions
import PySimpleGUI as sg
import time
import os

# Create file if it isn't exist
if not os.path.exists(functions.FILE_PATH):
    with open(functions.FILE_PATH, 'w') as file:
        pass

sg.theme("dark")
now = sg.Text("", key="clock")
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
layout = [[now],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('What do you want to do?',
                   layout=layout,
                   font=('Helvetica', 14))
while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(todos)
            window['todo'].update("")
        case "Complete":
            todo_to_complete = values['todos'][0]
            print(todo_to_complete)
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            break
        case "todos":
            selected_todo = values['todos'][0]
            window['todo'].update(selected_todo)
        case sg.WINDOW_CLOSED:
            break

window.close()
