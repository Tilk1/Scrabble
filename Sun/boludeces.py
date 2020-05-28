import PySimpleGUI as sg
import funciones


sg.theme('LightGrey1')  # please make your windows colorful

layout = [[sg.Text('Saber si existe la palabra:'), sg.Text(size=(12,1), key='-OUTPUT-'), sg.Button('Show'),],
          [sg.Input(key='-IN-')],
          [ sg.Button('Exit')]]

window = sg.Window('Window Title', layout)


layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-'), sg.Button('Show'),],
          [ sg.Button('Volver')]]

windowConfig = sg.Window('config', layout)



event, values = window.read()
while event is None or event == 'Exit':
    window.close()
    break
while event == 'Show':
    ingresado = values['-IN-']
    window['-OUTPUT-'].update(funciones.tipoPalabra(ingresado))
    event, values=window.read()
while event == 'Configuracion':
    window.hide()
       
