from pattern.text.es import verbs, tag, spelling, lexicon, parse
from sys import platform as _platform
import os
import PySimpleGUI as sg


# esto funciona mandandole un diccionario dentro de la funcion colocar fichas, con un formato asi {(7, 7): 'R.png', (7, 8): 'K.png', (7, 9): 'Z.png'}
def obtener_palabra(d):
    palabraFormada = ''
    for x in d:
        palabraFormada = palabraFormada + (d[x].split('.')[0])
    return(palabraFormada)


def clasificar(cual):
    if cual == "JJ":
        return "adjetivo"
    elif cual == "VB":
        return "verbo"
    elif cual != None:
        return 'sustantivo'


def tipoPalabra(d):
    palabra = obtener_palabra(d)
    analisis = parse(palabra, tags=True, chunks=False).split(' ')
    tipo = clasificar(analisis)
    if(tipo == 'sustantivo' or tipo == None):
        if not palabra.lower() in verbs:
            if not palabra.lower() in spelling:
                if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
                    return 'no_existe'
                else:
                    print('La encontró en lexicon')
                    return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
            else:
                print('La encontró en spelling')
                return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
        else:
            print('La encontró en verbs')
            return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
    else:
        return tipo


def calcularPuntaje(l, im, b):
    suma = 0
    multi = list()
    for x in l:
        cas = im[x]
        if (cas == 'lx2.png'):
            suma = suma+(b[l[x]]['valor']*2)
        elif(cas == 'lx3.png'):
            suma = suma+(b[l[x]]['valor']*3)
        elif(cas == '-1.png'):
            suma = suma+(b[l[x]]['valor']-1)
        elif(cas == '-2.png'):
            suma = suma+(b[l[x]]['valor']-2)
        elif(cas == '-3.png'):
            suma = suma+(b[l[x]]['valor']-3)
        elif(cas == 'px2.png'):
            multi.append(2)
        elif(cas == 'px3.png'):
            multi.append(3)
        else:
            suma = suma+b[l[x]]['valor']
    for y in multi:
        suma = suma*y
    return suma


def barraSistemaoperativo():
    if _platform.startswith == "win":  # windows
        return('/')
    else:  # linux
        return('/')


def carpetaImagenes():
    return os.getcwd() + barraSistemaoperativo() + 'imagenes' + barraSistemaoperativo()


def activarBotones(window):
    window.FindElement("comenzar").Update(visible=False, disabled=True)
    window["comenzar"].Update(visible=False, disabled=True)
    window["intercambiar"].Update(disabled=False)
    window["palabra"].Update(disabled=False)
    window["sacar"].Update(disabled=False)
    window["u0"].Update(disabled=False)
    window["u1"].Update(disabled=False)
    window["u2"].Update(disabled=False)
    window["u3"].Update(disabled=False)
    window["u4"].Update(disabled=False)
    window["u5"].Update(disabled=False)
    window["u6"].Update(disabled=False)
    window.FindElement("intercambiar").Widget.config(cursor="exchange")
    window.FindElement("palabra").Widget.config(cursor="heart")
    window.FindElement("sacar").Widget.config(cursor="pirate")
    window.FindElement("u0").Widget.config(cursor="hand2")
    window.FindElement("u1").Widget.config(cursor="hand2")
    window.FindElement("u2").Widget.config(cursor="hand2")
    window.FindElement("u3").Widget.config(cursor="hand2")
    window.FindElement("u4").Widget.config(cursor="hand2")
    window.FindElement("u5").Widget.config(cursor="hand2")
    window.FindElement("u6").Widget.config(cursor="hand2")


def mostrar_top10(puntajes):
    ancho_columnas = (10, 10)
    headings = ("NOMBRE", "PUNTAJE")
    columna = [
        [sg.Text(' ', text_color='black',
                 background_color='white', font=('Fixedsys', 5))],
        [sg.Text('1°', text_color='black',
                 background_color='white', font=('Fixedsys', 6))],
        [sg.Text('2°', text_color='black',
                 background_color='white', font=('Fixedsys', 6))],
        [sg.Text('3°', text_color='black',
                 background_color='white', font=('Fixedsys', 6))],
        [sg.Text('4°', text_color='black',
                 background_color='white', font=('Fixedsys', 6))],
        [sg.Text('5°', text_color='black',
                 background_color='white', font=('Fixedsys', 6))],
        [sg.Text('6°', text_color='black',
                 background_color='white', font=('Fixedsys', 6))],
        [sg.Text('7°', text_color='black',
                 background_color='white', font=('Fixedsys', 6))],
        [sg.Text('8°', text_color='black',
                 background_color='white', font=('Fixedsys', 6))],
    ]
    layout = [
        [sg.Text('TOP PUNTAJES ALTOS', font=('Fixedsys', 20),
                 text_color='salmon', background_color='white')],
        [sg.Column(columna, ""), sg.Table(puntajes, headings, select_mode="none", col_widths=ancho_columnas,
                                          num_rows=10, text_color="black", auto_size_columns=True, font=('Fixedsys', 6))],
        [sg.Text('   ', font=('Fixedsys', 18), background_color='white'), sg.Button(
            'VOLVER', font=('Fixedsys', 18), button_color=('orange', 'White'), key='jugar')],
    ]
    window = sg.Window("TOP 10", layout, resizable=True,
                       finalize=True).Finalize()
    while True:
        event, _values = window.read()
        if event is None:
            break
