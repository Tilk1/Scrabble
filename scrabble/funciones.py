from pattern.text.es import verbs, tag, spelling, lexicon, parse
from sys import platform as _platform
import os
import PySimpleGUI as sg

def tuplasString(diccio):
	t=dict()
	for x in diccio:
		t[str(x)]=diccio[x]
	return t

def tuplasInter(diccio):
	t=dict()
	for x in diccio:
		n=tuple(x.replace('(','').replace(')','').replace(' ','').replace(',',' ').split(' '))
		n=(int(n[0]),int(n[1]))
		print(x)
		print(diccio[x])
		t[n]=diccio[x]
	return t
	
def obtener_palabra(d):
    """
    Funciona mandandole un diccionario dentro de la funcion colocar fichas,
     el diccionario debe tener un formato asi {(7, 7): 'R.png', (7, 8): 'K.png', (7, 9): 'Z.png'}
     Obtiene la palabra sumando las letras sin lo que esta despues del punto. Es decir sin el .png de cada letra
    """
    palabraFormada = ''
    for x in d:
        palabraFormada = palabraFormada + (d[x].split('.')[0])
    return(palabraFormada)


def clasificar(cual):
    """
    Depende de la libreria pattern. El mismo utiliza JJ , VB y NN.
    IMPORTANTE: pattern considera sustantivo o NN todo loq no sea verbo o adjetivo.
    Por el motivo de arriba seria necesario  hacer una segunda comprobacion con lexicon o todo arrojaria sustantivo.
    Esto ultimo no se hace en esta funcion
    """
    if cual == "JJ":
        return "adjetivos"
    elif cual == "VB":
        return "verbos"
    else:
        return 'sustantivos'


def tipoPalabra(d):
    """
    Depende de la libreria pattern. El mismo utiliza JJ , VB y NN.
    IMPORTANTE: pattern considera sustantivo o NN todo loq no sea verbo o adjetivo.
    Por el motivo de arriba seria necesario  hacer una segunda comprobacion con lexicon o todo arrojaria sustantivo.
    Aqui se hace la segunda comprobacion con lexicon para clasificar si el sustantivo es realmente una palabra o simplemente
    entro en esa categoria y no existe.
    """
    palabra = obtener_palabra(d)
    analisis = parse(palabra, tags=True, chunks=False).split(' ')
    tipo = clasificar(analisis)
    if len(palabra) == 1:      #SIRVE PARA TESTEAR POR AHORA
        return 'no_existe'
    if(tipo == 'sustantivos'):
        if not palabra.lower() in verbs:
            if not palabra.lower() in spelling:
                if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
                    return 'no_existe'
                else:
                    return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
            else:
                return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
        else:
            return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
    else:
        return tipo


def calcularPuntaje(l, im, b): #l(puestas) im(tableroimagenes) b(bolsa)
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


def activarBotones(window):
    """
    Esta funcion activa los botones ya que:
    Los botones comienzan desactivados para evitar que el usuario clickee en ellos cuando la partida aun no comenzo.
    """
    window.FindElement("comenzar").Update(visible=False, disabled=True)
    window.FindElement('temporizador').Update(visible=True)
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


def mostrar_top10(hide,puntajes, configuracion):
    """
    Se encarga unicamente de la visualizacion de la ventana top10 
    """
    ancho_columnas = (10, 10)
    headings = ("NOMBRE", "PUNTAJE", "DIF", "FECHA")
    columna = [
        [sg.Image(os.path.join('imagenes','rankings.png'))],
    ]
    layout = [
        [sg.Text('TOP PUNTAJES ALTOS', font=('Fixedsys', 20),
                 text_color='salmon', background_color='white'), sg.Image(os.path.join('imagenes','trofeo.png'))],
        [sg.Column(columna, ""), sg.Table(puntajes, headings, select_mode="none", col_widths=ancho_columnas,
                                          num_rows=10, text_color="black", auto_size_columns=True, font=('Fixedsys', 6))],
        [sg.Text('      ', font=('Fixedsys', 18), background_color='white'), sg.Button(
            'VOLVER', font=('Fixedsys', 18), button_color=('orange', 'White'), key='volver')],
    ]
    top10 = sg.Window("TOP 10", layout, resizable=True,
                       finalize=True).Finalize()
    if(hide):
        top10.UnHide()
    while True:
        event, values = top10.read()
        print(event, values)
        if event == 'volver' or event == None:
            break
    top10.Hide()
    hide = True
    return hide, event

def activar_desactivar_Botones_basicos(window, boolean):
    """
    Recibe un booleano, si el booleano es true entonces desactiva los botones principales para jugar
    Si es falso entonces se pueden utilizar los botones
    """
    window["intercambiar"].Update(disabled=boolean)
    window["intercambiar"].Update(disabled=boolean)
    window["palabra"].Update(disabled=boolean)
    window["sacar"].Update(disabled=boolean)