import funciones
import PySimpleGUI as sg
import funcionesFichas as colocar
import random
import tableros
import configuraciones as con
import os
import json
import time
from multiprocessing import Process, Lock, Value
from ctypes import c_bool

global arranca_timer


def timer(n, lock):
    tiempo = [[sg.Image('imagenes/relojito.gif', key='relojito', background_color= 'White'), sg.Text('00:00', size=(8, 1), font=('Fixedsys', 20), justification='center', text_color='salmon',key='timer', background_color='white'),],]
    sg.theme_background_color(color='White')
    sg.theme_button_color(color=('White', 'White'))
    sg.theme_element_background_color(color='White')
    coordenadas = (70,31)
    #nuevas_coordenadas= (coordenadas[0]+980, coordenadas[1]+30)
    nuevas_coordenadas= (500,0)
    ventana_tiempo = sg.Window('temporizador', tiempo, no_titlebar=True, margins = (0,0) ,location= nuevas_coordenadas, keep_on_top= True)
    i = 12000
    image = ventana_tiempo['relojito']
    while n.value == False:
        time.sleep(0.10)  # ESPERA A LA SEÑAL
    while n.value == True:  #  RECIBO MENSAJE
        ventana_tiempo.read(10)
        ventana_tiempo['timer'].update('{:02d}:{:02d}:{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
        i = i - 1
        image.update_animation('imagenes/relojito.gif', 150)

def principal(n, lock):
    sg.theme_background_color(color='White')
    sg.theme_button_color(color=('Black', 'White'))
    sg.theme_element_background_color(color='White')
    # retorna el directorio donde estoy parado dependiendo OS + la carpeta imagenes
    cwd = funciones.carpetaImagenes()
    puntajeM = 0  # inicializacion puntaje usuario y maquina
    puntajeU = 0
    # diccionario con la imagen correspondiente a cada coordenada segun el tablero
    tableroIm = dict()
    # funcion para crear tablero, las coordenadas dependen de el tablero elegido en configuracion
    tablero = tableros.crearTablero(tableros.tablero1, 15, 15, tableroIm, sg)
    inicio = tableros.tablero1['play'][1]
    # fichas colocadas en el tablero de forma definitiva, es decir, palabras que fueron confirmadas
    tableroFichas = dict()
    bolsa = {'A.png': {'cant': 0, 'valor': 0},
            'B.png': {'cant': 0, 'valor': 0},
            'C.png': {'cant': 0, 'valor': 0},
            'D.png': {'cant': 0, 'valor': 0},
            'E.png': {'cant': 0, 'valor': 0},
            'F.png': {'cant': 0, 'valor': 0},
            'G.png': {'cant': 0, 'valor': 0},
            'H.png': {'cant': 0, 'valor': 0},
            'I.png': {'cant': 7, 'valor': 1},
            'J.png': {'cant': 7, 'valor': 1},
            'K.png': {'cant': 7, 'valor': 1},
            'L.png': {'cant': 7, 'valor': 1},
            'M.png': {'cant': 7, 'valor': 1},
            'N.png': {'cant': 7, 'valor': 1},
            'Ñ.png': {'cant': 7, 'valor': 1},
            'O.png': {'cant': 7, 'valor': 1},
            'P.png': {'cant': 7, 'valor': 1},
            'Q.png': {'cant': 7, 'valor': 1},
            'R.png': {'cant': 7, 'valor': 1},
            'S.png': {'cant': 7, 'valor': 1},
            'T.png': {'cant': 7, 'valor': 1},
            'U.png': {'cant': 7, 'valor': 1},
            'V.png': {'cant': 7, 'valor': 1},
            'W.png': {'cant': 7, 'valor': 1},
            'X.png': {'cant': 7, 'valor': 1},
            'Y.png': {'cant': 7, 'valor': 1},
            'Z.png': {'cant': 7, 'valor': 1},
            'LL.png': {'cant': 7, 'valor': 1},
            'RR.png': {'cant': 7, 'valor': 1}}
    # diccionario que lleva la cuenta de que iagen(letra) se encuentra en cada posicion del atril a todo momento
    letrasU = {'u0': '', 'u1': '', 'u2': '',
            'u3': '', 'u4': '', 'u5': '', 'u6': ''}
    letrasM = {'m0': '', 'm1': '', 'm2': '',
            'm3': '', 'm4': '', 'm5': '', 'm6': ''}
    texto_reporte = 'info sobre la partida'
    columna = [
        [sg.Text('', background_color='white')],
        [sg.Button(image_filename='bolsachica.png', border_width=0,key='intercambiar', disabled=True)],
        [sg.Button(image_filename='palabra.png', border_width=0,key='palabra', disabled=True)],
        [sg.Button(image_filename='sacar.png', border_width=0,key='sacar', disabled=True)]
    ]
    column1 = [
        [sg.Image('robot.png'), sg.Text('Puntaje: ', font=('Fixedsys', 17), text_color='orange', background_color='white', key='puntM'), sg.Button(image_filename='inicio.png', border_width=0, key='comenzar'), sg.Text(size=(7, 1), font=('Helvetica', 20), justification='center', key='temporizador', visible=False)],
        [sg.Button('', image_filename='color1.png', image_size=(46, 46), key='m0', disabled=True), sg.Button('', image_filename='color2.png', image_size=(46, 46), key='m1', disabled=True), sg.Button('', image_filename='color3.png', image_size=(46, 46), key='m2', disabled=True), sg.Button('', image_filename='color4.png', image_size=(46, 46), key='m3', disabled=True), sg.Button('', image_filename='color5.png', image_size=(46, 46), key='m4', disabled=True), sg.Button('', image_filename='color1.png', image_size=(46, 46), key='m5', disabled=True), sg.Button('', image_filename='color2.png', image_size=(46, 46), key='m6', disabled=True)],
        [sg.Column([[sg.Text(texto_reporte, text_color='black', key='reporte',background_color='lightblue', size=(30, 25))]]), sg.Column(columna)],
        [sg.Image('jugador.png'), sg.Text(text='Puntaje: 00 ', font=('Fixedsys', 17), text_color='orange', background_color='white', key='puntU')],
        [sg.Button('', image_filename='color1.png', image_size=(46, 46), key='u0', disabled=True), sg.Button('', image_filename='color2.png', image_size=(46, 46), key='u1', disabled=True), sg.Button('', image_filename='color3.png', image_size=(46, 46), key='u2', disabled=True), sg.Button('', image_filename='color4.png', image_size=(46, 46), key='u3', disabled=True), sg.Button('', image_filename='color5.png', image_size=(46, 46), key='u4', disabled=True), sg.Button('', image_filename='color1.png', image_size=(46, 46), key='u5', disabled=True), sg.Button('', image_filename='color2.png', image_size=(46, 46), key='u6', disabled=True)],
        [sg.Button(image_filename='terminar.png', key='exit', border_width=0), sg.Text('  ', background_color='white'), sg.Button(image_filename='posponer.png', key='posponer', border_width=0)]
    ]
    layout = [
        [sg.Column(tablero), sg.Column(column1)],  # tablero aca
    ]
    intercambiar = [
        [sg.Text('Cant de fichas a intercambiar')],
        [sg.Spin([i for i in range(1, 8)], initial_value=1, key='cant')],
        [sg.Button('Seleccionar cuales')]
    ]

    val = con.val1
    cant = con.cant1
    config = [
        [sg.Image('scrabblelogo.png')],
        [sg.Combo(['Nivel fácil', 'Nivel medio', 'Nivel difícil'], font=('Fixedsys', 17), text_color='salmon',background_color='white', key='niveles', enable_events=True, default_value='Nivel fácil')],
        [sg.Text('Tiempo: ', font=('Fixedsys', 15), text_color='salmon', background_color='white'), sg.Text('20seg', key='tiempo', font=('Fixedsys', 15), text_color='purple', background_color='white')],
        [sg.Text('Palabras posibles: ', font=('Fixedsys', 15), text_color='pink3', background_color='white'), sg.Text('sustantivos, adjetivos, verbos', key='palabras', font=('Fixedsys', 10), text_color='orange', background_color='white')],
        [sg.Text('Puntaje Letras: ', font=('Fixedsys', 15), text_color='lightblue', background_color='white'), sg.Combo(values=val, default_value=val[0], key='pun', font=('Fixedsys', 15), text_color='salmon', background_color='white')],
        [sg.Text('Cant letras: ', font=('Fixedsys', 15), text_color='orange', background_color='white'), sg.Combo(values=cant, default_value=cant[0], key='cant', font=('Fixedsys', 15), text_color='pink3', background_color='white')],
        [sg.Text('Tablero: ', font=('Fixedsys', 15), text_color='purple', background_color='white'), sg.Text('15x15', key='tab', font=('Fixedsys', 15), text_color='lightblue4', background_color='white')],
        [sg.Button('JUGAR', font=('Fixedsys', 18), button_color=('orange', 'White'), key='jugar'), sg.Button('CONFIGURAR', font=('Fixedsys', 18), button_color=('salmon', 'White'), key='config'), sg.Button('TOP10', font=('Fixedsys', 18), button_color=('lightblue', 'White'), key='top10')]
    ]

    # parte de abajo de las fichas, cuando comieza el juego o se quito la ficha para usarla
    colores = ['color1.png', 'color2.png',
            'color3.png', 'color4.png', 'color5.png']

    window = sg.Window('tablero', layout, grab_anywhere= True)
    popinter = sg.Window('intercambio', intercambiar)
    configuracion = sg.Window('config', config)

    

    # llama a elegirNivel me permite poder ver la configuracion predeterminada de los niveles en la interfaz
    event = con.elegirNivel(configuracion, bolsa)
    if(event == 'jugar'):
        configuracion.close()
        event, values = window.read()
        if(event == 'comenzar'):
            with lock:   # MANDO MENSAJE A ROBOT 2
                n.value = True
            funciones.activarBotones(window)
            # reparto fichas al usuario
            colocar.repartir(letrasU, bolsa, window, colores)
            # reparto fichas a la maquina
            colocar.repartir(letrasM, bolsa, window, colores)
            hide = False  # Para cunado necesito esconder la ventana de intercambio de fichas
            while(not event in ('exit', None)):
                puestas=dict() #Fichas que voy poniendo en el tablero en esa jugada
                event, valor = colocar.colocarFicha(tableroIm, tableroFichas, letrasU, window, colores, inicio, bolsa, puestas)  # comienza la jugada
                if(event == 'palabra'):
                    puntajeU = puntajeU+valor
                    texto_reporte = texto_reporte + '\n' + 'Usuario: ' + funciones.tipoPalabra(puestas) + ' ' + funciones.obtener_palabra(puestas) + ' ' +  str(valor) + ' puntos'  # /n es un espacio
                    window["reporte"].update(texto_reporte)
                    window['puntU'].update('Puntaje:'+str(puntajeU))
                    # vuelvo a repartir, si hay fichas restantes, van a quedar en el atril
                    colocar.repartir(letrasU, bolsa, window, colores)
                if(event == 'intercambiar'):
                    if(hide):
                        popinter.UnHide()
                    event, values = popinter.read()
                    popinter.Hide()
                    hide = True
                    colocar.intercambiarFichas(
                        letrasU, bolsa, window, values['cant'])
        elif(event == 'terminar'):
            window.close()
        else:
            event, values = window.read()
    elif(event == 'top10'):
        configuracion.close()
        try:
            with open("puntajes.json") as arc:
                datos = json.load(arc)
                if not datos:
                    sg.popup('Archivo de puntajes no encontrado')
                else:
                    puntajes = sorted(datos, reverse=True, key=lambda x: x[1])
                    funciones.mostrar_top10(puntajes)

        except FileNotFoundError:
            sg.popup('Archivo de puntajes no encontrado')

    window.close()



## MULTI THREADING  ###########################

def robot1(n, lock):
    principal(n, lock)

def robot2(n, lock):
    timer(n, lock)

if __name__ == '__main__':
    n = Value(c_bool, False)
    lock = Lock()
    Process(target=robot1, args=(n, lock)).start() 
    Process(target=robot2, args=(n, lock)).start()
