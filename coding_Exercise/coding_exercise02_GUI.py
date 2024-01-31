import PySimpleGUI as Sg

label1 = Sg.Text("Enter feel: ")
button1 = Sg.Input()

label2 = Sg.Text("Enter inches: ")
button2 = Sg.Input()

convert_button = Sg.Button("Convert")

window = Sg.Window("Convertor",
                   layout=[[label1, button1],
                           [label2, button2],
                           [convert_button]])

window.Read()
window.Close()
