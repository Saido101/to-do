import functions
import PySimpleGUI as ye

label = ye.Text("Type in a todo: ")
input_box = ye.InputText(tooltip="Enter todo", key="todo")
add_button = ye.Button("Add")
list_box = ye.Listbox(values=functions.get_todos(),
                      key="todos", enable_events=True, size=[45, 10])
edit_button = ye.Button("Edit")

window = ye.Window("My To-Do App", layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 10))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = value["todos"][0]
            new_todo = value["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window["todo"].update(value=value['todos'][0])
        case ye.WIN_CLOSED:
            break

window.close()