# ToDos Desktop GUI
import functions
import PySimpleGUI as Sg
import time
import os

if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", 'w') as file:
        pass

Sg.theme("DarkPurple4")

clock = Sg.Text('', key='clock')
label = Sg.Text("Type a ToDo")
input_box = Sg.InputText(tooltip="Enter ToDo", key="ToDo")
add_button = Sg.Button(key="Add", size=2, image_source='add.png',
                       mouseover_colors='LightBlue2', tooltip='Add ToDo')

list_box = Sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = Sg.Button("Edit")
complete_button = Sg.Button(key="Complete", size=2, image_source='complete.png',
                       mouseover_colors='LightBlue2', tooltip='Complete ToDo')
exit_button = Sg.Button("Exit")

window = Sg.Window('A random ToDo App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button, edit_button],
                           [list_box, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

# Just takes the time that the app was executed
# now = time.strftime("%b %d, %Y %H:%M")

while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    ## print(1, event)
    ## print(2, values)
    ## print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['ToDo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['ToDo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                Sg.popup("Please Select an item first", font=('Helvetica', 15))
        case "Complete":
            try:
                todos_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['ToDo'].update(value='')
            except IndexError:
                Sg.popup("Please Select an item first", font=('Helvetica', 15))
        case "Exit":
            break
        case 'todos':
            window['ToDo'].update(value=values['todos'][0])
        case Sg.WINDOW_CLOSED:
            break

# Close App
window.close()
