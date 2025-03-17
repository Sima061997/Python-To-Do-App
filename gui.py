import FreeSimpleGUI as sg

label = sg.Text("Give your To-Do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do-List App", layout=[[label], [input_box, add_button]], size=(500, 400))

window.read()
window.close()