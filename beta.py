import PySimpleGUI as sg
import funciones


sg.theme('LightGrey1')  # please make your windows colorful

tablero = []      ########GENERA TABLERO#######
for x in range(10):
    row = []
    for y in range(10):
        row.append(sg.RButton('',image_filename='images.png',size=(1,1),pad=(0,0),key= (x,y))) ##el filename no funciona
    tablero.append(row)

layout = [[sg.Text('Saber si existe la palabra:'), sg.Text(size=(12,1), key='-OUTPUT-'), sg.Button('Show'),],
          [sg.Input(key='-IN-')],
          [sg.Image(filename= '',key='image')],
          [sg.Button('CHECK'),sg.Column(tablero)], ##tablero aca
          [ sg.Button('Exit')]]

window = sg.Window('Window Title', layout)


layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-'), sg.Button('Show'),],
          [ sg.Button('Volver')]]

windowConfig = sg.Window('config', layout)


while True:  # Event Loop
    event, values = window.read()
    #print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Show':
        ingresado = values['-IN-']
        window['-OUTPUT-'].update(funciones.tipoPalabra(ingresado))
        #window['-OUTPUT-'].update(values['-IN-'])
    if event == 'Configuracion':
        window.hide()
       
window.close()