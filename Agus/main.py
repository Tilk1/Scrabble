import funciones
import PySimpleGUI as sg
import funcionesFichas as colocar
import random 
import tableros

sg.theme_background_color(color='DarkGrey')
sg.theme_button_color(color=('Black', 'DarkGrey'))
sg.theme_element_background_color(color='DarkGrey')


puntajeM=0  #inicializacion puntaje usuario y maquina
puntajeU=0
tableroIm=dict()   #diccionario con la imagen correspondiente a cada coordenada segun el tablero
tablero=tableros.crearTablero(tableros.tablero1, 15, 15, tableroIm, sg)  #funcion para crear tablero, las coordenadas dependen de el tablero elegido en configuracion 
tableroFichas=dict()    #fichas colocadas en el tablero de forma definitiva, es decir, palabras que fueron confirmadas
bolsa={'A.png':{'cant':11,'valor':1}, 'B.png':{'cant':11,'valor':1}, 'C.png':{'cant':8,'valor':1},'D.png':{'cant':7,'valor':1}, 'E.png':{'cant':7,'valor':1}, 'F.png':{'cant':7,'valor':1}, 'G.png':{'cant':7,'valor':1}, 'H.png':{'cant':5,'valor':1}, 'I.png':{'cant':7,'valor':1}, 'J.png':{'cant':7,'valor':1}, 'K.png':{'cant':7,'valor':1}, 'L.png':{'cant':7,'valor':1},'M.png':{'cant':7,'valor':1},'N.png':{'cant':7,'valor':1},'Ñ.png':{'cant':7,'valor':1},'O.png':{'cant':7,'valor':1},'P.png':{'cant':7,'valor':1},'Q.png':{'cant':7,'valor':1},'R.png':{'cant':7,'valor':1},'S.png':{'cant':7,'valor':1},'T.png':{'cant':7,'valor':1},'U.png':{'cant':7,'valor':1},'V.png':{'cant':7,'valor':1},'W.png':{'cant':7,'valor':1},'X.png':{'cant':7,'valor':1},'Y.png':{'cant':7,'valor':1},'Z.png':{'cant':7,'valor':1},'LL.png':{'cant':7,'valor':1},'RR.png':{'cant':7,'valor':1}}
letrasU={'u0':'', 'u1':'','u2':'','u3':'','u4':'','u5':'','u6':''}         #diccionario que lleva la cuenta de que iagen(letra) se encuentra en cada posicion del atril a todo momento
letrasM={'m0':'', 'm1':'','m2':'','m3':'','m4':'','m5':'','m6':''}
column1=[
		[sg.Button('inicio',border_width=0,font=('Fixedsys',18), key='comenzar')],
		[sg.Image('robot.png'), sg.Text('Puntaje: '), sg.Text('0', key='puntM')],
		[sg.Button('',image_filename='color1.png',image_size=(46, 46), key='m0'),sg.Button('',image_filename='color2.png',image_size=(46, 46),key='m1'),sg.Button('',image_filename='color3.png',image_size=(46, 46),key='m2'),sg.Button('',image_filename='color4.png',image_size=(46, 46),key='m3'),sg.Button('',image_filename='color5.png',image_size=(46, 46),key='m4'),sg.Button('',image_filename='color1.png',image_size=(46, 46),key='m5'),sg.Button('',image_filename='color2.png',image_size=(46, 46),key='m6')], 
		[sg.Text('',size=(30,10)),sg.Button(image_filename='bolsachica.png',border_width=0, key='intercambiar')],
		[sg.Image('jugador.png'), sg.Text('Puntaje: '), sg.Text('0', key='puntU'),sg.Button('palabra',font=('Fixedsys')),sg.Button('Sacar Todas',font=('Fixedsys'), key='sacar')],
		[sg.Button('',image_filename='color1.png',image_size=(46, 46), key='u0'),sg.Button('',image_filename='color2.png',image_size=(46, 46),key='u1'),sg.Button('',image_filename='color3.png',image_size=(46, 46), key='u2'),sg.Button('',image_filename='color4.png',image_size=(46, 46), key='u3'),sg.Button('',image_filename='color5.png',image_size=(46, 46), key='u4'),sg.Button('',image_filename='color1.png',image_size=(46, 46), key='u5'),sg.Button('',image_filename='color2.png',image_size=(46, 46), key='u6')],
		[sg.Button('Terminar',font=('Fixedsys'), size=(20,3), key='exit'),sg.Button('Posponer',font=('Fixedsys'), size=(20,3))]
		]
layout =[
		[sg.Column(tablero),sg.Column(column1)], ##tablero aca
		]
intercambiar=[
			[sg.Text('Cant de fichas a intercambiar')],
			[sg.Spin([i for i in range(1,8)], initial_value=1,key='cant')],
			[sg.Button('Aceptar')]
			]
val1=['A: 2', 'E: 2', 'O: 3', 'S: 3', 'I: 3', 'U: 3', 'N: 3', 'L: 3', 'R: 3', 'T: 3', 'C: 3', 'D: 3', 'G: 3', 'M: 4', 'B: 4', 'P: 4', 'F: 5', 'H: 5', 'V: 5', 'Y: 5', 'J: 7', 'K: 9', 'L: 9','L: 9', 'Ñ: 9', 'Q: 9', 'RR: 9', 'W: 9', 'X: 9','Z: 11']
cant1=['A: 11', 'E: 11', 'O: 8', 'S: 7', 'I: 8', 'U: 8', 'N: 5', 'L: 4', 'R: 4', 'T: 4', 'C: 4', 'D: 4', 'G: 2', 'M: 3', 'B: 6', 'P: 2', 'F: 2', 'H: 2', 'V: 2', 'Y: 1', 'J: 2', 'K: 1''LL: 1', 'Ñ: 1', 'Q: 1', 'RR: 1', 'W: 1', 'X: 1','Z: 1']

val2=['A: 1', 'E: 1', 'O: 2', 'S: 2', 'I: 2', 'U: 2', 'N: 2', 'L: 2', 'R: 2', 'T: 2', 'C: 2', 'D: 2', 'G: 2', 'M: 3', 'B: 3', 'P: 3', 'F: 4', 'H: 4', 'V: 4', 'Y: 4', 'J: 6', 'K: 8', 'L: 8','L: 8', 'Ñ: 8', 'Q: 8', 'RR: 8', 'W: 8', 'X: 8','Z: 10']
cant2=['A: 9', 'E: 9', 'O: 6', 'S: 5', 'I: 4', 'U: 4', 'N: 5', 'L: 4', 'R: 4', 'T: 4', 'C: 4', 'D: 4', 'G: 2', 'M: 3', 'B: 4', 'P: 2', 'F: 2', 'H: 2', 'V: 2', 'Y: 1', 'J: 2', 'K: 2', 'LL: 1', 'Ñ: 1', 'Q: 2', 'RR: 2', 'W: 1', 'X: 2','Z: 2']

val3=['A: 1', 'E: 1', 'O: 1', 'S: 1', 'I: 1', 'U: 1', 'N: 1', 'L: 1', 'R: 1', 'T: 1', 'C: 1', 'D: 1', 'G: 1', 'M: 2', 'B: 2' 'P: 2', 'F: 3', 'H: 3', 'V: 3', 'Y: 3', 'J: 5', 'K: 7', 'L: 7','L: 7', 'Ñ: 7', 'Q: 7', 'RR: 7', 'W: 7', 'X: 7','Z: 9']
cant3=['A: 7', 'E: 7', 'O: 4', 'S: 5', 'I: 4', 'U: 4', 'N: 5', 'L: 4', 'R: 4', 'T: 4', 'C: 4', 'D: 4', 'G: 2', 'M: 3', 'B: 3', 'P: 2', 'F: 2', 'H: 4', 'V: 3', 'Y: 3', 'J: 3', 'K: 3','LL: 3', 'Ñ: 2', 'Q: 3', 'RR: 3', 'W: 2', 'X: 3','Z: 3']

config=[
		[sg.Text('SCRIBBLE',font=('Fixedsys',30))],
		[sg.Combo(['Nivel 1', 'Nivel 2', 'Nivel 3'], key='niveles', default_value='Nivel 1')],
		[sg.Text('Tiempo: '), sg.Text('20seg', key='tiempo')],
		[sg.Text('Palabras posibles: '), sg.Text('sustantivos, adjetivos, verbos', key='palabras')],
		[sg.Text('Puntaje Letras: '), sg.Combo(val1, default_value=val1[0])],
		[sg.Text('Cant letras: '), sg.Combo(bolsa, default_value=cant1[0])],
		[sg.Text('Tablero: '), sg.Text('15x20', key='tab')],
		[sg.Button('JUGAR',font=('Fixedsys',18), key='jugar'), sg.Button('CONFIGURAR',font=('Fixedsys',18), key='config'),sg.Button('TOP10',font=('Fixedsys',18), key='top10')]
		]

colores= ['color1.png','color2.png','color3.png','color4.png','color5.png']  #parte de abajo de las fichas, cuando comieza el juego o se quito la ficha para usarla

window = sg.Window('tablero', layout)
popinter = sg.Window('intercambio', intercambiar)
configuracion=sg.Window('config', config)

event, values = configuracion.read()
if(event=='jugar'):
	configuracion.close()
	event, values = window.read()
	while(not event in ('exit', None)):
		if(event=='comenzar'):	
			colocar.repartir(letrasU, bolsa, window, colores) #reparto fichas al usuario
			colocar.repartir(letrasM, bolsa, window, colores) #reparto fichas a la maquina
			hide = False  #Para cunado necesito esconder la ventana de intercambio de fichas
			while True:
				event, letrasPal, valor=colocar.colocarFicha(tableroIm,tableroFichas,letrasU, window,colores,tableros.tablero2['play'][1], bolsa) #comienza la jugada
				if(event=='palabra'):
					puntajeU=puntajeU+valor
					window['puntU'].update(str(puntajeU))
					colocar.repartir(letrasU, bolsa, window, colores)  #vuelvo a repartir, si hay fichas restantes, van a quedar en el atril
				if(event=='intercambiar'):
					if(hide):
						popinter.UnHide()
					event, values= popinter.read()
					popinter.Hide()
					hide=True
					colocar.intercambiarFichas(letrasU, bolsa, window, values['cant'])
				event, values = window.read()	
		else:
			event, values = window.read()
elif(event=='config'):
	configuracion.close()

window.close()
