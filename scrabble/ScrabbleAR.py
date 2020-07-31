import funciones
import PySimpleGUI as sg
import funcionesFichas as colocar
import random
import configuraciones as con
import os
import json
import time
from multiprocessing import Process, Lock, Value
from ctypes import c_bool
import compu

global arranca_timer


def timer(n, lock):
    tiempo = [[sg.Image(os.path.join('imagenes','relojito.gif'), key='relojito', background_color= 'White'), sg.Text('00:00', size=(8, 1), font=('Fixedsys', 20), justification='center', text_color='salmon',key='timer', background_color='white'),],]
    sg.theme_background_color(color='White')
    sg.theme_button_color(color=('White', 'White'))
    sg.theme_element_background_color(color='White')
    nuevas_coordenadas= (500,0)
    ventana_tiempo = sg.Window('temporizador', tiempo, no_titlebar=True, margins = (0,0) ,location= nuevas_coordenadas, keep_on_top= True)
    i = 12000
    image = ventana_tiempo['relojito']
    while n.value == False:  # ESPERA EL MENSAJE DE ROBOT1
        time.sleep(0.10)  
    while n.value == True:  #  RECIBO MENSAJE ENTONCES COMIENZO
        ventana_tiempo.read(10)
        ventana_tiempo['timer'].update('{:02d}:{:02d}:{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
        i = i - 1
        image.update_animation(os.path.join('imagenes','relojito.gif'), 150)
    ventana_tiempo.close()

def principal(n, lock):
    sg.theme_background_color(color='White')
    sg.theme_button_color(color=('Black', 'White'))
    sg.theme_element_background_color(color='White')
    puntajeM = 0  # inicializacion puntaje usuario y maquina
    puntajeU = 0
    # diccionario con la imagen correspondiente a cada coordenada segun el tablero
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
        [sg.Button(image_filename=(os.path.join('imagenes','bolsachica.png')), border_width=0,key='intercambiar', disabled=True)],
        [sg.Button(image_filename=(os.path.join('imagenes','palabra.png')), border_width=0,key='palabra', disabled=True)],
        [sg.Button(image_filename=(os.path.join('imagenes','sacar.png')), border_width=0,key='sacar', disabled=True)]
    ]
    column1 = [
        [sg.Image(os.path.join('imagenes','robot.gif'), key = 'gifcompu'), sg.Text('Puntaje: ', font=('Fixedsys', 17), text_color='orange', background_color='white', key='puntM'), sg.Button(image_filename=os.path.join('imagenes','inicio.png'), border_width=0, key='comenzar'), sg.Text(size=(7, 1), font=('Helvetica', 20), justification='center', key='temporizador', visible=False)],
        [sg.Button('', image_filename=os.path.join('imagenes','color1.png'), image_size=(46, 46), key='m0', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color2.png'), image_size=(46, 46), key='m1', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color3.png'), image_size=(46, 46), key='m2', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color4.png'), image_size=(46, 46), key='m3', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color5.png'), image_size=(46, 46), key='m4', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color1.png'), image_size=(46, 46), key='m5', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color2.png'), image_size=(46, 46), key='m6', disabled=True)],
        [sg.Column([[sg.Text(texto_reporte, text_color='black', key='reporte',background_color='lightblue', size=(30, 500))]], scrollable= True, vertical_scroll_only= True, size = (250,400)), sg.Column(columna)],
        [sg.Image(os.path.join('imagenes','jugador.png')), sg.Text(text='Puntaje: 00 ', font=('Fixedsys', 17), text_color='orange', background_color='white', key='puntU')],
        [sg.Button('', image_filename=os.path.join('imagenes','color1.png'), image_size=(46, 46), key='u0', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color2.png'), image_size=(46, 46), key='u1', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color3.png'), image_size=(46, 46), key='u2', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color4.png'), image_size=(46, 46), key='u3', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color5.png'), image_size=(46, 46), key='u4', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color1.png'), image_size=(46, 46), key='u5', disabled=True), sg.Button('', image_filename=os.path.join('imagenes','color2.png'), image_size=(46, 46), key='u6', disabled=True)],
        [sg.Button(image_filename=os.path.join('imagenes','terminar.png'), key='exit', border_width=0), sg.Text('  ', background_color='white'), sg.Button(image_filename=os.path.join('imagenes','posponer.png'), key='posponer', border_width=0)]
    ]
    
    intercambiar = [
        [sg.Text('Cant de fichas a intercambiar')],
        [sg.Spin([i for i in range(1, 8)], initial_value=1, key='cant')],
        [sg.Button('Seleccionar cuales')]
    ]

    val = con.val1
    cant = con.cant1
    layoutmenu = [
        [sg.Image(os.path.join('imagenes','scrabblelogo.png'))],
        [sg.Combo(['Nivel fácil', 'Nivel medio', 'Nivel difícil'], font=('Fixedsys', 17), text_color='salmon',background_color='white', key='niveles', enable_events=True, default_value='Nivel fácil')],
        [sg.Text('Tiempo: ', font=('Fixedsys', 15), text_color='salmon', background_color='white'), sg.Text('8min', key='tiempo', font=('Fixedsys', 15), text_color='purple', background_color='white')],
        [sg.Text('Palabras posibles: ', font=('Fixedsys', 15), text_color='pink3', background_color='white'), sg.Text('sustantivos/adjetivos/verbos', key='palabras', font=('Fixedsys', 10), text_color='orange', background_color='white')],
        [sg.Text('Puntaje Letras: ', font=('Fixedsys', 15), text_color='lightblue', background_color='white'), sg.Combo(values=list(val.keys()),enable_events=True, default_value=list(val.keys())[0], key='pun', font=('Fixedsys', 15), text_color='salmon', background_color='white'),sg.Text(val['A'],key='punV')],
        [sg.Text('Cant letras: ', font=('Fixedsys', 15), text_color='orange', background_color='white'), sg.Combo(values=list(cant.keys()),enable_events=True, default_value=list(cant.keys())[0], key='cant', font=('Fixedsys', 15), text_color='pink3', background_color='white'),sg.Text(cant['A'],key='cantV')],
        [sg.Text('Tablero: ', font=('Fixedsys', 15), text_color='purple', background_color='white'), sg.Text('15x15', key='tab', font=('Fixedsys', 15), text_color='lightblue4', background_color='white')],
        [sg.Button('JUGAR', font=('Fixedsys', 18), button_color=('orange', 'White'), key='jugar'), sg.Button('CONFIGURAR', font=('Fixedsys', 18), button_color=('salmon', 'White'), key='configurar'), sg.Button('TOP10', font=('Fixedsys', 18), button_color=('lightblue', 'White'), key='top10')]
    ]
    row1 = [sg.Text('    ',font=('Fixedsys',12),text_color='white', background_color='white'),sg.Image(os.path.join('imagenes','letras.png'), background_color='white')]
    row2 = [sg.Text('valor',font=('Fixedsys',12),text_color='pink3', background_color='white')]
    row3 = [sg.Text('cant ',font=('Fixedsys',12),text_color='lightblue', background_color='white')]
    for y in val.keys():
        row2.append(sg.Combo(values=[x for x in range(1, 21)],default_value=1, key='valor', font=('Fixedsys', 15), text_color='purple', background_color='white'))
        row3.append(sg.Combo(values=[x for x in range(1, 21)],default_value=1, key='cant', font=('Fixedsys', 15), text_color='purple', background_color='white'))
    config = [
        [sg.Image(os.path.join('imagenes','configtitulo.png'))],    
        row1,
        row2,
        row3,
        [sg.Text('Tiempo: ', font=('Fixedsys', 15), text_color='orange', background_color='white'), sg.Combo(values=[x for x in range(1, 61)], default_value=1,key='time', font=('Fixedsys', 15), text_color='purple', background_color='white'),sg.Text('min', font=('Fixedsys', 15), text_color='salmon', background_color='white')],
        [sg.Text('Palabras posibles: ', font=('Fixedsys', 15), text_color='salmon', background_color='white'), sg.Combo(values=['Adjetivos','Sustantivos','Verbos','Adjetivos/Sustantivos/Verbos', 'Sustantivos/Verbos','Adjetivos/Sustantivos','Adjetivos/Verbos'],default_value='Adjetivo', key='tiposP', font=('Fixedsys', 15), text_color='purple', background_color='white')],
        [sg.Text('Tablero: ', font=('Fixedsys', 15), text_color='purple', background_color='white'), sg.Combo(values=[(15,15),(15,17),(15,20)],default_value=(15,15), key='table', font=('Fixedsys', 15), text_color='purple', background_color='white')],
        [sg.Button('JUGAR', font=('Fixedsys', 18), button_color=('orange', 'White'), key='jugar')]
    ]   
    # parte de abajo de las fichas, cuando comieza el juego o se quito la ficha para usarla
    colores = ['color1.png','color2.png',
            'color3.png','color4.png','color5.png']

    popinter = sg.Window('intercambio', intercambiar)
    menu = sg.Window('MENU', layoutmenu)
    configuracion = sg.Window('config', config)
    
    tableroIm = dict()
    # llama a elegirNivel me permite poder ver la configuracion predeterminada de los niveles en la interfaz
    event,t,palabras,tab = con.elegirNivel(menu, bolsa)
    palabras=palabras.split('/')
    # funcion para crear tablero, las coordenadas dependen de el tablero elegido en configuracion
    if(event!='configurar'):
        inicio, window=con.cofigtab(tab,column1,tableroIm)
    while(not event in (None, 'exit')):
        if(event == 'jugar'):
            menu.close()
            event, values = window.read()
            if(event == 'comenzar'):
                with lock:   # mando mensaje para comenzar timer
                    n.value = True
                funciones.activarBotones(window)
                # reparto fichas al usuario
                colocar.repartir(letrasU, bolsa, window)
                # reparto fichas a la maquina
                colocar.repartir(letrasM, bolsa, window)
                hide = False  # Para cunado necesito esconder la ventana de intercambio de fichas
                while(not event in ('exit', None)):
                    puestas=dict() #Fichas que voy poniendo en el tablero en esa jugada
                    event, valor = colocar.colocarFicha(tableroIm, tableroFichas, letrasU, window, colores, inicio, bolsa, puestas,palabras)  # comienza la jugada
                    if(event == 'palabra'):
                        puntajeU = puntajeU+valor
                        texto_reporte = texto_reporte + '\n' + 'Usuario: ' + funciones.tipoPalabra(puestas) + ' ' + funciones.obtener_palabra(puestas) + ' ' +  str(valor) + ' puntos'  # /n es un espacio
                        window["reporte"].update(texto_reporte)
                        window['puntU'].update('Puntaje:'+str(puntajeU))
                        # vuelvo a repartir, si hay fichas restantes, van a quedar en el atril
                        colocar.repartir(letrasU, bolsa, window)
                    if(event == 'intercambiar'):
                        if(hide):
                            popinter.UnHide()
                        event, values = popinter.read()
                        popinter.Hide()
                        hide = True
                        colocar.intercambiarFichas(
                            letrasU, bolsa, window, values['cant'])
                    compu.turno_maquina(tableroIm, tableroFichas, letrasM, window, colores, bolsa)
            elif(event == 'terminar'):
                window.close()
            else:
                event, values = window.read()
        elif(event =='configurar'):
            menu.close()
            event, values = configuracion.read()
            while(event!='jugar'):
                event, values = configuracion.read()
            con.configcustom(bolsa, -1, list(val.keys()), values, 'valor')
            con.configcustom(bolsa, 27, list(cant.keys()), values, 'cant')
            inicio, window=con.cofigtab(values['table'],column1,tableroIm)
            t=values['time']
            palabras=values['tiposP']
            palabras=palabras.split('/')
        elif(event == 'top10'):
            menu.hide()
            try:
                with open("puntajes.json") as arc:
                    datos = json.load(arc)
                    if not datos:
                        sg.popup('Archivo de puntajes no encontrado')
                    else:
                        puntajes = sorted(datos, reverse=True, key=lambda x: x[1])
                        funciones.mostrar_top10(puntajes,menu)

            except FileNotFoundError:
                sg.popup('Archivo de puntajes no encontrado')
        

    with lock:   # mando mensaje a robot2 para que se cierre
        n.value = False
    window.close()




## MULTI THREADING  ###########################

def robot1(n, lock):
    principal(n, lock)

def robot2(n, lock):
    timer(n, lock)

if __name__ == '__main__':
    n = Value(c_bool, False) # Mensaje de robots para comenzar o parar timer
    lock = Lock()
    Process(target=robot1, args=(n, lock)).start() 
    Process(target=robot2, args=(n, lock)).start()