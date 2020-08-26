import PySimpleGUI as sg
import tableros 

def configLetras(c, a, bolsa): #agrega los cambios a la bolsa
    """
    Se actualiza la bolsa de letras segun las letras individuales que se eligieron en la configuración
    
    """
    for x in c:
        bolsa[x+'.png'][a] = c[x]

def cofigtab(tab,column1,tableroIm):
    """
    Se crea el tablero segun las dimensiones de tablero que se elijen en el menu o en configuración.
    Retorna el boton de inicio de ese tablero y la window, ya lista.
    """
    if(tab==(15,15)):
        tipotab=tableros.tablero1   #Se elige el tipo de tablero según las dimensiones elegidas
    elif(tab==(15,17)):
        tipotab=tableros.tablero2
    elif(tab==(15,20)):
        tipotab=tableros.tablero3
    tablero = tableros.crearTablero(tipotab, tab[0], tab[1], tableroIm, sg)  #llamo funcion crearTablero para crearlo, me actualiza tableroIm que tiene las imagenes del tablero, según cada coordenada
    inicio = tipotab['play'][1]   #botón de inicio, donde debe pasar la primera palabra del juego entero
    layout = [
        [sg.Column(tablero), sg.Column(column1)],  # tablero aca
    ]
    window = sg.Window('tablero', layout, grab_anywhere= True)  #creo la window con el layout correspondiente
    return inicio, window

def configcustom(bolsa, c, a, values, cual):
    """
    Paso a la bolsa original, cada letra a la cual le asigné un valor y cantidad en configuración
    cual puede ser cant o valor, segun lo que quiera guardar en la bolsa, si los valores de las letras o las cantidades.
    num y c son valores dependiendo del diccionario values, cuando se lee la window de configuración.

    """
    num=c
    for n in a:
        if(num==c):
            bolsa[n+'.png'][cual]=values[cual]
        else:
            bolsa[n+'.png'][cual]=values[cual+str(num)]
        num=num+1

def elegirNivel(win, bolsa):
    """
    Función que lee la window menú. Permite elegir los distintos niveles, Fácil, Medio o Difícil.
    Retorna los valores de las variables configuradas event,tiempo,palabras,tab, nivel.

    """
    event, values = win.read()
    val = val1
    cant = cant1
    tiempo=8
    tab=(15,15)
    nivel='Nivel fácil'
    palabras='sustantivos/adjetivos/verbos'
    while(not event in ('jugar', 'configurar', 'top10', None)):  #mientras no se intente salir del menú o comenzar el juego, muestro los distintos valores por defecto de los niveles
        if(event == 'niveles'):
            if('Nivel fácil' == values['niveles']):
                nivel=values['niveles']
                tiempo=8
                palabras='sustantivos/adjetivos/verbos'
                tab=(15,15)
                win['tiempo'].update('8min')                               #actualizo la interfaz para que
                win['palabras'].update('sustantivos/adjetivos/verbos')
                win['pun'].update(values=list(val1.keys()))
                win['cant'].update(values=list(cant1.keys()))
                win['punV'].update(val1['A'])
                win['cantV'].update(cant1['A'])
                win['tab'].update('15x15')
                val = val1
                cant = cant1
            elif('Nivel medio' == values['niveles']):
                nivel=values['niveles']
                tiempo=6
                palabras='sustantivos/adjetivos/verbos'
                tab=(15,17)
                win['tiempo'].update('6min')
                win['palabras'].update('sustantivos/adjetivos/verbos')
                win['pun'].update(values=list(val2.keys()))
                win['cant'].update(values=list(cant2.keys()))
                win['punV'].update(val2['A'])
                win['cantV'].update(cant2['A'])
                win['tab'].update('15x17')
                val = val2
                cant = cant2
            elif('Nivel difícil' == values['niveles']):
                nivel=values['niveles']
                tiempo=4
                palabras='sustantivos/adjetivos/verbos'
                tab=(15,20)
                win['tiempo'].update('4min')
                win['palabras'].update('sustantivos/adjetivos/verbos')
                win['pun'].update(values=list(val3.keys()))
                win['cant'].update(values=list(cant3.keys()))
                win['punV'].update(val3['A'])
                win['cantV'].update(cant3['A'])
                win['tab'].update('15x20')
                val = val3
                cant = cant3
        elif(event == 'pun'):
            win['punV'].update(val[values['pun']])
        elif(event=='cant'):
             win['cantV'].update(cant[values['cant']])
        event, values = win.read()
    configLetras(val, 'valor', bolsa)
    configLetras(cant, 'cant', bolsa)
    return event,tiempo,palabras,tab, nivel


# niveles, letras valor y cantidad predeterminado

val1 = {'A': 2, 'E': 2, 'O': 3, 'S': 3, 'I': 3, 'U': 3, 'N': 3, 'L': 9, 'R': 3, 'T': 3, 'C': 3, 'D': 3, 'G': 3, 'M': 4, 'B': 4, 'P': 4, 'F': 5, 'H': 5, 'V': 5, 'Y':5, 'J': 7, 'K': 9, 'Ñ': 9, 'Q': 9, 'RR': 9, 'W': 9, 'X': 9, 'Z': 11,'LL': 9}
cant1 = {'A': 11, 'E': 11, 'O': 8, 'S': 7, 'I': 8, 'U': 8, 'N': 5, 'L': 4, 'R': 4, 'T': 4, 'C': 4, 'D': 4, 'G': 2, 'M': 3, 'B': 6, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'Y': 1, 'J': 2, 'K': 1, 'Ñ': 1, 'Q': 1, 'RR': 1, 'W': 1, 'X': 1, 'Z': 1,'LL': 1}

val2 = {'A': 1, 'E': 1, 'O': 2, 'S': 2, 'I': 2, 'U': 2, 'N': 2, 'L': 8, 'R': 2, 'T': 2, 'C': 2, 'D': 2, 'G': 2, 'M': 3, 'B': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'Y':4, 'J': 6, 'K': 8, 'Ñ': 8, 'Q': 8, 'RR': 8, 'W': 8, 'X': 8, 'Z': 10,'LL': 8}
cant2 = {'A': 9, 'E': 9, 'O': 6, 'S': 5, 'I': 4, 'U': 4, 'N': 5, 'L': 4, 'R': 4, 'T': 4, 'C': 4, 'D': 4, 'G': 2, 'M': 3, 'B': 4, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'Y':1, 'J': 2, 'K': 2, 'Ñ': 1, 'Q': 2, 'RR': 2, 'W': 1, 'X': 2, 'Z': 2,'LL': 1}

val3 = {'A': 1, 'E': 1, 'O': 1, 'S': 1, 'I': 1, 'U': 1, 'N': 1, 'L': 7, 'R': 1, 'T': 1, 'C': 1, 'D': 1, 'G': 1, 'M': 2, 'B': 2, 'P': 2, 'F': 3, 'H': 3, 'V': 3, 'Y':3, 'J': 5, 'K': 7, 'Ñ': 7, 'Q': 7, 'RR': 7, 'W': 7, 'X': 7, 'Z': 9,'LL': 7}
cant3 = {'A': 7, 'E': 7, 'O': 4, 'S': 5, 'I': 4, 'U': 4, 'N': 5, 'L': 4, 'R': 4, 'T': 4, 'C': 4, 'D': 4, 'G': 2, 'M': 3, 'B': 3, 'P': 2, 'F': 2, 'H': 4, 'V': 3, 'Y':3, 'J': 3, 'K': 3, 'Ñ': 2, 'Q': 3, 'RR': 3, 'W': 2, 'X': 3, 'Z': 3,'LL': 3}
