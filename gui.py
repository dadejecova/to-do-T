# ToDos Desktop GUI
import time
import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a ToDo")
input_box = Sg.InputText(tooltip="Enter ToDo", key="ToDo")
add_button = Sg.Button("Add")

list_box = Sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = Sg.Button("Edit")

window = Sg.Window('My ToDo App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15))

# Just takes the time that the app was executed
now = time.strftime("%b %d, %Y %H:%M")

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['ToDo'] + " - " + now + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['ToDo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['ToDo'].update(value=values['todos'][0])
        case Sg.WINDOW_CLOSED:
            break


window.close()
