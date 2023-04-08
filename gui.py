import functions
import PySimpleGUI as ye

label = ye.Text("Type in a todo: ")
input_box = ye.InputText(tooltip="Enter todo")
add_button = ye.Button("Add")

window = ye.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()