import functions
import FreeSimpleGUI as sg

label = sg.Text("Give your To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="-TODO_INPUT-")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='0',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do-List App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, remove_button],
                           [exit_button]],

                   size=(500, 400))


#So that the program doesn't gets close on any click on GUI
while True:
  event, values = window.read()
  print(1, event)
  print(2, values)
  print(3, values['0'])

  match event:
    case "Add":
      todos = functions.get_todos()
      new_todo = values["-TODO_INPUT-"] + "\n"
      if new_todo:
        todos.append(new_todo)
        functions.write_todos(todos)
        window["0"].update(values=todos)
        window["-TODO_INPUT-"].update("")

    case "Edit":
      try:
        todo_to_edit = values["0"][0]
        new_todo = values["-TODO_INPUT-"] + "\n"
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window["0"].update(values=todos)
      except IndexError:
        sg.popup("Please select the item first.", font=("Helvetica", 20))

    case "Remove":
      try:
        todo_to_remove = values["0"][0]
        todos = functions.get_todos()
        todos.remove(todo_to_remove)
        functions.write_todos(todos)
        window["0"].update(values=todos)
        window["-TODO_INPUT-"].update(value="")
      except IndexError:
        sg.popup("Please select the item first.", font=("Helvetica", 20))

    case "Exit":
      break

    case sg.WIN_CLOSED:
      break

window.close()