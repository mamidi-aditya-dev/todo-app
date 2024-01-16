import PySimpleGUI as sg
lable = sg.Text("Type In The Todo")
input_box = sg.Input(tooltip= "enter todo")
add_button = sg.Button("ADD")

windows = sg.Window('MY TODO APP ', layout = [[lable], [input_box,add_button]])
windows.read()
windows.close()