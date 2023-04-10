import functions
import PySimpleGUI as ye
import time

ye.theme("Black")
clock = ye.Text('', key='clock')
label = ye.Text("Type in a todo: ")
input_box = ye.InputText(tooltip="Enter todo", key="todo")
add_button = ye.Button("Add")
list_box = ye.Listbox(values=functions.get_todos(),
                      key="todos", enable_events=True, size=[45, 10])
edit_button = ye.Button("Edit")
complete_button = ye.Button("Complete")
exit_button = ye.Button("Exit")

window = ye.Window("My To-Do App", layout=[[clock],
                                           [label],
                                           [input_box, add_button],
                                           [list_box, edit_button, complete_button],
                                           [exit_button]],
                   font=("Helvetica", 10))

while True:
    event, value = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%A %B %m %d %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = value["todos"][0]
                new_todo = value["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                ye.popup("Please select an item", font=("Helvetica", 10))

        case "Complete":
            try:
                todo_to_remove = value["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                ye.popup("Please select an item", font=("Helvetica", 10))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=value['todos'][0])
        case ye.WIN_CLOSED:
            break

window.close()