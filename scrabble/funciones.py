#from pattern.text.es import verbs, tag, spelling, lexicon, parse
from sys import platform as _platform
import os
import PySimpleGUI as sg
import json
from datetime import date
import pickle

cwd = os.getcwd()


def tuplasString(diccio):
	"""
	Convierte los indices(keys) de un diccionario que son tuplas a strings.
	Se utiliza para cuando se pospone la partida, ya que JSON solo permite keys de tipo integer o string en el diccionario.
	Los diccionarios tableroFichas(mantiene las fichas colocadas de forma definitiva en el tablero) y tableroIm(Imagenes del tablero)
	tienen como keys las coordenadas del tablero, que son tuplas.

	"""
	t=dict()
	for x in diccio:
		t[str(x)]=diccio[x]
	return t

def tuplasInter(diccio):
	"""
	Las keys del diccionario que son tuplas en forma de string se pasan a tuplas, con numeros, para recrear el diccionario original, 
	una vez hecho el load desde el archivo txt.

	"""
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
	file = open(os.path.join(cwd,'lista_palabras_arg.pickle'), 'rb')
	data = pickle.load(file)
	file.close()
	file = open(os.path.join(cwd,'lista_verbos_sin_acento.pickle'), 'rb')
	data2 = pickle.load(file)
	file.close()
	palabra = obtener_palabra(d)
	if palabra in data or palabra in data2:
		return 'sustantivos'
	else:
		return 'no_existe'


def calcularPuntaje(l, im, b): #l(puestas) im(tableroimagenes) b(bolsa)
	"""
	Calcula el puntaje segun el valor de cada letra y la casilla del tablero en la que está posicionado.
	Cuando una letra esta en una casilla de multiplicar la palabra, se guarda en una lista las multiplicaciones que
	corresponden y luego se hacen a la suma entera.

	"""
	suma = 0
	multi = list()
	for x in l:
		cas = im[x]
		if (cas == 'lx2.png'):    #se suman a las letras la casilla en particular en la que esta posicionada
			suma = suma+(b[l[x]]['valor']*2)
		elif(cas == 'lx3.png'):
			suma = suma+(b[l[x]]['valor']*3)
		elif(cas == '-1.png'):
			suma = suma+(b[l[x]]['valor']-1)
		elif(cas == '-2.png'):
			suma = suma+(b[l[x]]['valor']-2)
		elif(cas == '-3.png'):
			suma = suma+(b[l[x]]['valor']-3)
		else:
			suma = suma+b[l[x]]['valor']   #Si la casilla no es de premio, entonces a suma se le agrega el valor de la letra. Cuando esta pos en una casilla de multiplicar 
			if(cas == 'px2.png'):		   #la palabra, esta se aplica a la palabra entera y no a la letra en particular, por lo que se suma su valor y se agrega a la lista la multiplicación
				multi.append(2)
			elif(cas == 'px3.png'):
				multi.append(3)
	for y in multi:
		suma = suma*y   #multiplico las casillas de palabrax2 o palabrax3
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
		[sg.Image(os.path.join(cwd,'rankings.png'))],
	]
	layout = [
		[sg.Text('   TOP PUNTAJES ALTOS', font=('Fixedsys', 20),
				 text_color='salmon', background_color='white'), sg.Image(os.path.join(cwd,'trofeo.png'))],
		[sg.Column(columna, ""), sg.Table(puntajes, headings, select_mode="none", col_widths=ancho_columnas,
										  num_rows=10, text_color="black", auto_size_columns=True, font=('Fixedsys', 6))],
		[sg.Text('         ', font=('Fixedsys', 18), background_color='white'), sg.Button(
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


def cargar(puntajeU,name,nivel):
	"""
	Recibe algunos datos de la partida para colocar en el top10 en caso de superar
	el puntaje del que esta ultimo.(Con json una lista verificando el ultimo elemento)

	"""
	print('ENTROO A CARGAR')
	try:
		with open(os.path.join(cwd,"puntajes.json")) as arc:
			datos = json.load(arc)
			if not datos:
				sg.popup('Archivo de puntajes no encontrado')
			else:
				puntajes = sorted(datos, reverse=False, key=lambda x: x[1])

	except FileNotFoundError:
		sg.popup('Archivo de puntajes no encontrado')
	
	if puntajeU > puntajes[0][1]:
		quedotop10 = True
	else:
		quedotop10 = False
		print('FALSOO')

	if quedotop10 == True:
		with open(os.path.join(cwd,'puntajes.json'),'w') as arc2:  #quito al ultimo
			print('LEEE 1111')
			puntajes[0][0] = name
			puntajes[0][2] = nivel
			json.dump(puntajes, arc2)
	  
def mostrar_fin_partida(puntajeU,puntajeM):
	"""
	Recibe algunos datos de la partida para colocar en el top10 en caso de superar
	el puntaje del que esta ultimo. (Con json una lista verificando el ultimo elemento)
	Tambien muestra la ultima ventana final para ver tu puntaje y si entraste al top 10
	"""
	try:
		with open((os.path.join(cwd,"puntajes.json"))) as arc:
			datos = json.load(arc)
			if not datos:
				sg.popup('Archivo de puntajes no encontrado')
			else:
				puntajes = sorted(datos, reverse=False, key=lambda x: x[1])

	except FileNotFoundError:
		sg.popup('Archivo de puntajes no encontrado')

	# me fijo si supera al mas bajo de todos para quedar en el top 10
	if puntajeU > puntajes[0][1]:
		quedotop10 = True
	else:
		quedotop10 = False

	if quedotop10 == True:
		with open(os.path.join(cwd,'puntajes.json'),'w') as arc2:  #quito al ultimo
			print('LEEE 222')
			today = date.today()
			puntajes[0][1] = puntajeU      # puntaje
			puntajes[0][3] = str(today)    #fecha
			json.dump(puntajes, arc2)

	# agrego el nuevo puntaje una vez que lo haya escrito y toco el boton OK
	#puntajes.append = ["juuuu",  999, "easy", "3/3/2050"]
	#print(puntajes) 

	color_usuario = 'red'
	color_compu = 'red'

	if puntajeU > puntajeM:
		ganador = 'Usuario'
		imagen_ganador = 'jugador.png'
		color_usuario = 'green'
	else:
		ganador = 'Computadora'
		imagen_ganador = 'robot.gif'
		color_compu = 'green'


	layout = [
		[sg.Text('¡La partida ha terminado!', font=('Fixedsys', 30),text_color='salmon', background_color='white')],
		[sg.Text('       Has quedado en el top 10', font=('Fixedsys', 20),text_color='green', background_color='white', visible = quedotop10)],
		[sg.Text('No alcanzaste para quedar en el top 10', font=('Fixedsys', 20),text_color='red', background_color='white', visible = not(quedotop10))],
		[sg.Text('',background_color= 'White')],
		[sg.Text('Ganador: ', font=('Fixedsys', 17),text_color='salmon', background_color='white'), sg.Text(ganador, font=('Fixedsys', 17),text_color='salmon', background_color='white'),sg.Image(os.path.join(cwd,imagen_ganador))],
		[sg.Text('',background_color= 'White')],
		[sg.Text('Puntuacion Usuario    :', font=('Fixedsys', 17),text_color='salmon', background_color='white'),sg.Text(str(puntajeU), font=('Fixedsys', 20),text_color=color_usuario, background_color='white')],
		[sg.Text('Puntuacion Computadora:', font=('Fixedsys', 17),text_color='salmon', background_color='white'),sg.Text(str(puntajeM), font=('Fixedsys', 20),text_color=color_compu, background_color='white')],
		[sg.Text('Escribe tu nombre', font=('Fixedsys', 20),text_color='salmon', background_color='white', visible= False),sg.Input(size=(12,8),font=('Fixedsys', 17),visible= False),sg.Button('OK', size=(5,2), font=('Fixedsys', 15), button_color=('orange', 'White'), key='volver',visible= False)],
		[sg.Text('      ', font=('Fixedsys', 45),background_color= 'White'), sg.Button('SALIR', font=('Fixedsys', 18), button_color=('orange', 'White'), key='salir2',visible=False)],
			]

	fin_partida = sg.Window("fin", layout, resizable=True,finalize=True)
	while True:
		event, values = fin_partida.read()
		fin_partida.UnHide()
		print(event,values)
		if event == 'salir2' or event == None:
			break
	fin_partida.Close()