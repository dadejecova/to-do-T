# ToDos Desktop GUI
import time
import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a ToDo")
input_box = Sg.InputText(tooltip="Enter ToDo", key="ToDo")
add_button = Sg.Button("Add")

window = Sg.Window('My ToDo App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15))

# Just takes the time that the app was executed
now = time.strftime("%b %d, %Y %H:%M:%S")

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['ToDo'] + " " + now + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case Sg.WINDOW_CLOSED:
            break


window.close()
