import multiprocessing
import time
import PySimpleGUI as sg

tiempo = [[sg.Button(image_filename='imagenes/reloj.png', border_width=0, key='relojito'), sg.Text('00:00', size=(8, 1), font=('Fixedsys', 23), justification='center', text_color='white',
                        key='timer', background_color='black'),],
                        ]

sg.theme_background_color(color='White')
sg.theme_button_color(color=('White', 'White'))
sg.theme_element_background_color(color='White')

coordenadas = (70,31)


nuevas_coordenadas= (coordenadas[0]+800, coordenadas[1]-28)


ventana_tiempo = sg.Window('temporizador', tiempo, no_titlebar=True, default_element_size=(40, 1),location= nuevas_coordenadas)



i = 12000
while True:
    button, values = ventana_tiempo.read(10)
    ventana_tiempo['timer'].update('{:02d}:{:02d}:{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
    i = i - 1






