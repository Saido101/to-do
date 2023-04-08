import functions
import PySimpleGUI as ye

label = ye.Text("Type in a todo: ")
input_box = ye.InputText(tooltip="Enter todo", key="todo")
add_button = ye.Button("Add")

window = ye.Window("My To-Do App", layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 15))

while True:
    event, value = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case ye.WIN_CLOSED:
            break

window.close()