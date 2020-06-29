import funciones
import PySimpleGUI as sg
import funcionesFichas as colocar
import random 
import tableros
import configuraciones as con
sg.theme_background_color(color='White')
sg.theme_button_color(color=('Black', 'White'))
sg.theme_element_background_color(color='White')


puntajeM=0  #inicializacion puntaje usuario y maquina
puntajeU=0
tableroIm=dict()   #diccionario con la imagen correspondiente a cada coordenada segun el tablero
tablero=tableros.crearTablero(tableros.tablero1, 15, 15, tableroIm, sg)  #funcion para crear tablero, las coordenadas dependen de el tablero elegido en configuracion 
inicio=tableros.tablero1['play'][1]
tableroFichas=dict()    #fichas colocadas en el tablero de forma definitiva, es decir, palabras que fueron confirmadas
bolsa={'A.png':{'cant':11,'valor':2}, 'B.png':{'cant':6,'valor':4}, 'C.png':{'cant':4,'valor':3},'D.png':{'cant':7,'valor':1}, 'E.png':{'cant':7,'valor':1}, 'F.png':{'cant':7,'valor':1}, 'G.png':{'cant':7,'valor':1}, 'H.png':{'cant':5,'valor':1}, 'I.png':{'cant':7,'valor':1}, 'J.png':{'cant':7,'valor':1}, 'K.png':{'cant':7,'valor':1}, 'L.png':{'cant':7,'valor':1},'M.png':{'cant':7,'valor':1},'N.png':{'cant':7,'valor':1},'Ñ.png':{'cant':7,'valor':1},'O.png':{'cant':7,'valor':1},'P.png':{'cant':7,'valor':1},'Q.png':{'cant':7,'valor':1},'R.png':{'cant':7,'valor':1},'S.png':{'cant':7,'valor':1},'T.png':{'cant':7,'valor':1},'U.png':{'cant':7,'valor':1},'V.png':{'cant':7,'valor':1},'W.png':{'cant':7,'valor':1},'X.png':{'cant':7,'valor':1},'Y.png':{'cant':7,'valor':1},'Z.png':{'cant':7,'valor':1},'LL.png':{'cant':7,'valor':1},'RR.png':{'cant':7,'valor':1}}
letrasU={'u0':'', 'u1':'','u2':'','u3':'','u4':'','u5':'','u6':''}         #diccionario que lleva la cuenta de que iagen(letra) se encuentra en cada posicion del atril a todo momento
letrasM={'m0':'', 'm1':'','m2':'','m3':'','m4':'','m5':'','m6':''}
columna=[
		[sg.Text('',background_color='white')],
		[sg.Button(image_filename='bolsachica.png',border_width=0, key='intercambiar')],
		[sg.Button(image_filename='palabra.png',border_width=0, key='palabra')],
		[sg.Button(image_filename='sacar.png',border_width=0, key='sacar')]
		]
column1=[
		[sg.Image('robot.png'), sg.Text('Puntaje: ',font=('Fixedsys',17),text_color='orange',background_color='white'), sg.Text('0',font=('Fixedsys',17),text_color='black',background_color='white', key='puntM'),sg.Button(image_filename='inicio.png',border_width=0, key='comenzar')],
		[sg.Button('',image_filename='color1.png',image_size=(46, 46), key='m0'),sg.Button('',image_filename='color2.png',image_size=(46, 46),key='m1'),sg.Button('',image_filename='color3.png',image_size=(46, 46),key='m2'),sg.Button('',image_filename='color4.png',image_size=(46, 46),key='m3'),sg.Button('',image_filename='color5.png',image_size=(46, 46),key='m4'),sg.Button('',image_filename='color1.png',image_size=(46, 46),key='m5'),sg.Button('',image_filename='color2.png',image_size=(46, 46),key='m6')], 
		[sg.Column([[sg.Text('info sobre la partida y palabras q se ingresan',text_color='black',background_color='lightblue',size=(30,25))]]),sg.Column(columna)],
		[sg.Image('jugador.png'), sg.Text('Puntaje: ',font=('Fixedsys',17),text_color='orange',background_color='white'), sg.Text('0',font=('Fixedsys',17),text_color='black',background_color='white', key='puntU')],
		[sg.Button('',image_filename='color1.png',image_size=(46, 46), key='u0'),sg.Button('',image_filename='color2.png',image_size=(46, 46),key='u1'),sg.Button('',image_filename='color3.png',image_size=(46, 46), key='u2'),sg.Button('',image_filename='color4.png',image_size=(46, 46), key='u3'),sg.Button('',image_filename='color5.png',image_size=(46, 46), key='u4'),sg.Button('',image_filename='color1.png',image_size=(46, 46), key='u5'),sg.Button('',image_filename='color2.png',image_size=(46, 46), key='u6')],
		[sg.Button(image_filename='terminar.png', key='exit',border_width=0),sg.Text('  ',background_color='white'),sg.Button(image_filename='posponer.png',key='posponer',border_width=0)]
		]
layout =[
		[sg.Column(tablero),sg.Column(column1)], ##tablero aca
		]
intercambiar=[
			[sg.Text('Cant de fichas a intercambiar')],
			[sg.Spin([i for i in range(1,8)], initial_value=1,key='cant')],
			[sg.Button('Aceptar')]
			]

val=con.val1
cant=con.cant1
config=[
		[sg.Image('scrabblelogo.png')],
		[sg.Combo(['Nivel fácil', 'Nivel medio', 'Nivel difícil'],font=('Fixedsys',17),text_color='salmon',background_color='white', key='niveles', enable_events=True,default_value='Nivel fácil')],
		[sg.Text('Tiempo: ',font=('Fixedsys',17),text_color='salmon',background_color='white'), sg.Text('20seg', key='tiempo')],
		[sg.Text('Palabras posibles: '), sg.Text('sustantivos, adjetivos, verbos', key='palabras',font=('Fixedsys',10),text_color='orange',background_color='white')],
		[sg.Text('Puntaje Letras: '), sg.Combo(values=val, default_value=val[0], key='pun')],
		[sg.Text('Cant letras: '), sg.Combo(values=cant, default_value=cant[0], key='cant')],
		[sg.Text('Tablero: '), sg.Text('15x15', key='tab')],
		[sg.Button('JUGAR',font=('Fixedsys',18), button_color=('orange', 'White'),key='jugar'), sg.Button('CONFIGURAR',font=('Fixedsys',18),button_color=('salmon', 'White') ,key='config'),sg.Button('TOP10',font=('Fixedsys',18),button_color=('lightblue', 'White'),key='top10')]
		]

colores= ['color1.png','color2.png','color3.png','color4.png','color5.png']  #parte de abajo de las fichas, cuando comieza el juego o se quito la ficha para usarla

window = sg.Window('tablero', layout)
popinter = sg.Window('intercambio', intercambiar)
configuracion=sg.Window('config', config)

event=con.elegirNivel(configuracion,val,cant)
if(event=='jugar'):
	configuracion.close()
	event, values = window.read()
	if(event=='comenzar'):	
		colocar.repartir(letrasU, bolsa, window, colores) #reparto fichas al usuario
		colocar.repartir(letrasM, bolsa, window, colores) #reparto fichas a la maquina
		hide = False  #Para cunado necesito esconder la ventana de intercambio de fichas
		while(not event in ('exit', None)):
			event, letrasPal, valor=colocar.colocarFicha(tableroIm,tableroFichas,letrasU, window,colores,inicio, bolsa) #comienza la jugada
			if(event=='palabra'):
				print(valor)
				puntajeU=puntajeU+valor
				print(puntajeU)
				window['puntU'].update(puntajeU)
				colocar.repartir(letrasU, bolsa, window, colores)  #vuelvo a repartir, si hay fichas restantes, van a quedar en el atril
			if(event=='intercambiar'):
				if(hide):
					popinter.UnHide()
				event, values= popinter.read()
				popinter.Hide()
				hide=True
				colocar.intercambiarFichas(letrasU, bolsa, window, values['cant'])	
	else:
		event, values = window.read()
elif(event=='config'):
	configuracion.close()

window.close()
