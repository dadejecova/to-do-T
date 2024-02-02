import PySimpleGUI as Sg

label1 = Sg.Text("Enter feel: ")
button1 = Sg.Input(key="feet_data")

label2 = Sg.Text("Enter inches: ")
button2 = Sg.Input(key="inches_data")

convert_button = Sg.Button("Convert")
label3 = Sg.Text(key="Result")

exit_button = Sg.Button("Exit")

window = Sg.Window("Convertor",
                   layout=[[label1, button1],
                           [label2, button2],
                           [convert_button, exit_button, label3]])
new_meters = 0
while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case Sg.WINDOW_CLOSED:
            break
    #print(1, event)
    #print(2, values)
    #print(3, values['feet_data'])
    #print(4, values['inches_data'])
    try:
        feet_int = float(values['feet_data'])
        inches_int = float(values['inches_data'])
        new_meters = feet_int * 0.3048 + inches_int * 0.0254
        window['Result'].update(new_meters)
    except ValueError:
        Sg.popup("Please provide two numbers.", font=("Helvetica", 10))


window.Close()