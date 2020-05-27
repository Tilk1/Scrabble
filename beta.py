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
#test#kjasdjkadnkjansd probando mucho texto
#kjasdjkadnkjansd probando mucho texto#kjasdjkadnkjansd probando mucho texto

#kjasdjkadnkjansd probando mucho texto#kjasdjkadnkjansd probando 

#kjasdjkadnkjansd probando mucho texto
#kjasdjkadnkjansd probando mucho texto