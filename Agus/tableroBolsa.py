import funciones
import PySimpleGUI as sg
import random
sg.theme_background_color(color='Lavender')
sg.theme_button_color(color=('Lavender', 'Lavender'))
sg.theme_element_background_color(color='Lavender')


def randomLetra(bolsa):
    otro = True
    while(otro):
        letra = random.choice(list(bolsa))
        if(bolsa[letra]['cant'] > 0):
            otro = False
            bolsa[letra]['cant'] = bolsa[letra]['cant']-1
    return letra


def repartir(letras, bolsa, window, colores):
	for x in letras:
		if(letras[x]=='' or letras[x] in colores):
			letra=randomLetra(bolsa)
			if(x.find('u')!=-1):
				window[x].update(image_filename=letra)
			letras[x]=letra

def intercambiarFichas(letras, bolsa, window, cant):
	if(cant==7):
		for x in letras:
			letra=randomLetra(bolsa)
			window[x].update(image_filename=letra)
			bolsa[letras[x]]['cant']=bolsa[letras[x]]['cant']+1
			letras[x]=letra
	else:
		cambios=list()
		for _ in range(cant):
			sigo=True
			while(sigo):
				event, values=window.read()
				if not event in cambios:
					cambios.append(event)
					sigo=False
			letra=randomLetra(bolsa)
			window[event].update(image_filename=letra)
			letras[event]=letra
			bolsa[letras[event]]['cant']=bolsa[letras[event]]['cant']+1
	sg.popup('Intercambio realizado!')

def ponerFicha(window,letra, tableroF, puestas, event):
	window[event].update(image_filename=letra)
	puestas[event]=letra
	return False
def colocarFicha(tableroI,tableroF,letras, window, colores, primerF):
	print(tableroF)
	originales=letras.copy()  #Fichas del atril que tenia en el comienzo de la jugada
	puestas=dict()            #Fichas que voy poniendo en el tablero en esa jugada
	poner=False				  #Poner va a ser True cuando tenga una letra en mano para poner en el tablero
	letra=''		          #No tengo ninguna letra en mano, lo inicializo en ''
	direc='definir'
	nro=0						#Nro de ficha que esta poniendo
	event, values = window.read()
	while not event in (None,'Exit','palabra','intercambiar'):
		if event in ('u0', 'u1','u2','u3','u4','u5','u6'):  				#Si selecciono una letra
			if ((letras[event] in colores) and (originales[event]==letra)):  #Si en el diccionario letras que guarda la imagen actual de la ficha, es un color, pero lo estoy selecionando, signofica que quiero volver a poner la letra en su lugar
				window[event].update(image_filename=letra)					 #originales[event]==letra corrobora que la estoy poniendo en la misma pos original. Hago un update de la ficha en la interfaz con la letra
				letras[event]=letra
				letra=''   													#Como no tengo ninguna letra en mano, la pongo en ''
			elif((not letras[event] in colores) and (letra=='')):   #Si la ficha tiene una aletra y no tiene un color, y no tengo ninguna letra en mano(corroboro esto asi no la pierdo en caso de haber agarrado una y no haber hecho nada con ella), entonces la agarro
				letra=letras[event]   								#letra la actualizo con la de la ficha
				color=random.choice(colores)   						#pongo un color en la ficha que agarre, "queda vacia"
				window[event].update(image_filename=color)
				letras[event]=color    								#en el diccionario donde tengo las imag de las fichas pongo que tengo un color
				poner=True
		elif(isinstance(event, tuple)):    							#Si toco el tablero
			if(poner and letra!=''):    							#Si tengo una ficha en mano (poner=True) y (letra!='')
				if(primerF):            							#Si es la primera ficha de toda la partida entonces la puedo poner solo en UN lugar
					if(event==(0,0)):
						poner=ponerFicha(window, letra, tableroF, puestas, event)   #Llamo al metodo ponerFicha que actualiza en el tablero la letra
						nro=nro+1    												#Sumo +1 porq agregue una ficha al tablero
						primerF=False  												#Como ya lo puse en el lugar inicial lo pongo en falso
						letra=''      												#No tengo ninguna ficha en mano porq la puse en el tablero, entonces letra=''
						ficha=event 												#ficha la uso para saber en que pos puedo poner la siguiente letra
				elif(event in tableroF):    													#Si estoy intentando poner la ficha arriba de una de otra partida
					sg.popup('No puede colocar una ficha sobre una de una jugada anterior')
				elif(event in puestas):
					sg.popup('No puede colocar la letra en un lugar ocupado, retirela si lo desea')   	#Si intento poner una ficha sobre las ya puestas en esa jugada
				else: 									
					correcta=True											#correcta me dice si elegi un lugar del tablero correcto para poner la ficha
					if(nro==0):      										#La primera es en caso de cuando no es la primera jugada de toda la partida
						ficha=event
					elif(nro==1):											#La segunda ficha determina en que dieccion voy a poner el resto, si a izquierda o derecha
						if(event==(ficha[0]+1,ficha[1])):   					
							direc='abajo'
							ficha=(ficha[0]+1,ficha[1])
						elif(event==(ficha[0],ficha[1]+1)):
							direc='izq'
							ficha=(ficha[0],ficha[1]+1)
						else:
							correcta=False													#correcto es False cuando intento poner una ficha en un lugar que no sea abajo o a izq de la primera ficha
					elif(nro>=2):   														#Si estoy colocando las fichas que sean a partir de la 2>=
						if((direc=='abajo') and (event==(ficha[0]+1,ficha[1]))):  			#Si la ficha la estoy queriendo poner a izquierda y la direccion es a la izquierda
							ficha=(ficha[0]+1,ficha[1])                                     #actualizo la ficha, donde voy a ponerla en el tablero, ya que la estaba intentando poner correctamente
						elif((direc=='izq') and (event==(ficha[0],ficha[1]+1))):    		#Lo mismo pero para abajo
							ficha=(ficha[0],ficha[1]+1)
						else:
							correcta=False													#correcto es False cuando intento poner una ficha en un lugar que no sea abajo o a izq de la 2 ficha o mayores
					if(correcta):         													#Si ino intente poner una ficha en una direccion incorrecta
						poner=ponerFicha(window, letra, tableroF, puestas, ficha)    		#La coloco en el tablero segun la ficha que use 
						nro=nro+1
						letra=''
			else:                            
				if((event in puestas) and (event==ficha)):        													#Si no tengo una ficha en mano, pero toco una ficha colocada en el tablero
					sacar=sg.popup_yes_no('Quiere sacar la ficha?')
					if(sacar=='Yes'):    														#Si quiero sacar la ficha
						window[event].update(image_filename=tableroI[event])  					#Pongo en donde estaba la ficha, la imagen del tablero original sin nada
						l=list(filter(lambda x:x[1]==puestas[event],list(originales.items())))[0][0]  		#Busco en el dict originales, cual de las fichas del atril, tenia la letra que puse en el tablero, y en l queda la key de la ficha, por ejemplo 'u2'
						window[l].update(image_filename=puestas[event])   									#Pongo en el atril la ficha en la interfaz
						letras[l]=puestas[event]    														#Vuelvo a poner en e dict de letras la letra segun corresponda a su posicion en el atril
						puestas.pop(event)          														#sacas la letra de las que pusiste en el tablero, ya que no esta mas
						if(direc=='izq'):      																#la pos del tablero en donde podes poner va a ser -1 ya que en donde estaba la ficha ya no esta
							ficha=(ficha[0],ficha[1]-1)
						elif(direc=='abajo'):
							ficha=(ficha[0]-1,ficha[1])
						nro=nro-1																			#Como saco una ficha, el nro de ficha puesto es -1, de esta forma puedo volver a elegir la direccion si saco la 2da ficha de la palabra y si saco la primera ficha, poder seguir poniendo fichas(Si saco la primera y nro es >2 va  asuponer que hay una direccion o que habia una ficha previa puesta con la cual calcularla)
				elif(not event in (tableroF, puestas)):      												#Si no tenes una letra en mano y estas tocando un lugar en donde no hay nada
					sg.popup('No ha seleccionado una ficha para colocar')
		event, values = window.read()
	if(event=='palabra'):
		for x in puestas:
			tableroF[x]=puestas[x]
	return primerF, event
puntajeM='0'
puntajeU='0'
tableroIm=dict()
vacios= ['vacio.png','vacio1.png','vacio2.png','vacio3.png','vacio4.png','vacio5.png','vacio6.png','vacio7.png']
tablero = []      ########GENERA TABLERO#######
for x in range(10):
	row = []
	for y in range(10):
		im=random.choice(vacios)
		tableroIm[(x,y)]=im
		row.append(sg.RButton('',image_filename=im,border_width=0,image_size=(50, 50),size=(50,50),pad=(0,0),key=(x,y))) ##el filename no funciona
	tablero.append(row)
tableroFichas=dict()
bolsa={'A.png':{'cant':11,'valor':1}, 'B.png':{'cant':11,'valor':3}, 'C.png':{'cant':8,'valor':1},'D.png':{'cant':7,'valor':1}, 'E.png':{'cant':7,'valor':1}, 'F.png':{'cant':7,'valor':1}, 'G.png':{'cant':7,'valor':1}, 'H.png':{'cant':5,'valor':1}, 'I.png':{'cant':7,'valor':1}, 'J.png':{'cant':7,'valor':1}, 'K.png':{'cant':7,'valor':1}, 'L.png':{'cant':7,'valor':1},'M.png':{'cant':7,'valor':1},'N.png':{'cant':7,'valor':1},'Ñ.png':{'cant':7,'valor':1},'O.png':{'cant':7,'valor':1},'P.png':{'cant':7,'valor':1},'Q.png':{'cant':7,'valor':1},'R.png':{'cant':7,'valor':1},'S.png':{'cant':7,'valor':1},'T.png':{'cant':7,'valor':1},'U.png':{'cant':7,'valor':1},'V.png':{'cant':7,'valor':1},'W.png':{'cant':7,'valor':1},'X.png':{'cant':7,'valor':1},'Y.png':{'cant':7,'valor':1},'Z.png':{'cant':7,'valor':1},'LL.png':{'cant':7,'valor':1},'RR.png':{'cant':7,'valor':1}}
letrasU={'u0':'', 'u1':'','u2':'','u3':'','u4':'','u5':'','u6':''}
letrasM={'m0':'', 'm1':'','m2':'','m3':'','m4':'','m5':'','m6':''}
column1=[
		[sg.Button('Exit',font=('Fixedsys'), size=(20,3))], 
		[sg.Button('palabra',font=('Fixedsys'))],
		[sg.Image('bolsachica.png')],
		[sg.Button('',image_filename='intercambiar.png',border_width=0,font=('Fixedsys'), key='intercambiar')]
		]
layout =[
		[sg.Text('Puntaje: '),sg.Text(puntajeM)],
		[sg.Image('robot.png'),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='m0',size=(50,50)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='m1', size=(4,2)),sg.Button('',image_filename='color3.png',image_size=(50, 50),key='m2', size=(4,2)),sg.Button('',image_filename='color4.png',image_size=(50, 50),key='m3', size=(4,2)),sg.Button('',image_filename='color5.png',image_size=(50, 50),key='m4', size=(4,2)),sg.Button('',image_filename='color1.png',image_size=(50, 50),key='m5',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='m6', size=(4,2)),sg.Text(' ', background_color='Lavender'),sg.Button('',image_filename='comenzar.png',border_width=0,font=('Fixedsys',18), key='comenzar')],
		[sg.Column(tablero),sg.Column(column1)], ##tablero aca
		[sg.Image('jugador.png'),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='u0',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='u1', size=(4,2)),sg.Button('',image_filename='color3.png',image_size=(50, 50), key='u2', size=(4,2)),sg.Button('',image_filename='color4.png',image_size=(50, 50), key='u3', size=(4,2)),sg.Button('',image_filename='color5.png',image_size=(50, 50), key='u4', size=(4,2)),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='u5',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50), key='u6', size=(4,2))],
		[sg.Text('Puntaje: '),sg.Text(puntajeU)]
		]
intercambiar=[
			[sg.Text('Cant de fichas a intercambiar')],
			[sg.Spin([i for i in range(1,8)], initial_value=1,key='cant')],
			[sg.Button('Aceptar')]
			]

colores= ['color1.png','color2.png','color3.png','color4.png','color5.png']

window = sg.Window('tablero', layout)
popinter = sg.Window('intercambio', intercambiar)
event, values = window.read()
primer=True
if(event=='comenzar'):
	repartir(letrasU, bolsa, window, colores)
	repartir(letrasM, bolsa, window, colores)
	hide = False
	while True:
		primer, event=colocarFicha(tableroIm,tableroFichas,letrasU, window,colores, primer)
		if(event=='palabra'):
			repartir(letrasU, bolsa, window, colores)
		if(event=='intercambiar'):
			if(hide):
				popinter.UnHide()
			event, values= popinter.read()
			popinter.Hide()
			hide=True
			intercambiarFichas(letrasU, bolsa, window, values['cant'])
		if event in (None, 'Exit'):
			break 	
window.close()
