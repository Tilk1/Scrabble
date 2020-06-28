import random
import PySimpleGUI as sg
import funciones

bolsa={'A.png':{'cant':11,'valor':1}, 'B.png':{'cant':11,'valor':1}, 'C.png':{'cant':8,'valor':1},'D.png':{'cant':7,'valor':1}, 'E.png':{'cant':7,'valor':1}, 'F.png':{'cant':7,'valor':1}, 'G.png':{'cant':7,'valor':1}, 'H.png':{'cant':5,'valor':1}, 'I.png':{'cant':7,'valor':1}, 'J.png':{'cant':7,'valor':1}, 'K.png':{'cant':7,'valor':1}, 'L.png':{'cant':7,'valor':1},'M.png':{'cant':7,'valor':1},'N.png':{'cant':7,'valor':1},'Ñ.png':{'cant':7,'valor':1},'O.png':{'cant':7,'valor':1},'P.png':{'cant':7,'valor':1},'Q.png':{'cant':7,'valor':1},'R.png':{'cant':7,'valor':1},'S.png':{'cant':7,'valor':1},'T.png':{'cant':7,'valor':1},'U.png':{'cant':7,'valor':1},'V.png':{'cant':7,'valor':1},'W.png':{'cant':7,'valor':1},'X.png':{'cant':7,'valor':1},'Y.png':{'cant':7,'valor':1},'Z.png':{'cant':7,'valor':1},'LL.png':{'cant':7,'valor':1},'RR.png':{'cant':7,'valor':1}}
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
				event,_=window.read()
				if not event in cambios:
					cambios.append(event)
					sigo=False
			letra=randomLetra(bolsa)
			window[event].update(image_filename=letra)
			letras[event]=letra
			bolsa[letras[event]]['cant']=bolsa[letras[event]]['cant']+1
	sg.popup('Intercambio realizado!')

def ponerFicha(window,letra, puestas, event):
	window[event].update(image_filename=letra)
	puestas[event]=letra
	return False

def sacarFicha(tableroI, puestas, originales, letras, event, window):
	if(event=='sacar'):     #saco todas las fichas
		for y in puestas:
			for x in originales:
				if (originales[x]==puestas[y]):
					window[y].update(image_filename=tableroI[y])							#Pongo en donde estaba la ficha, la imagen del tablero original sin nada
					window[x].update(image_filename=originales[x])							#Pongo en el atril la ficha en la interfaz
					letras[x]=originales[x]    												#Vuelvo a poner en el dict de letras la letra segun corresponda a su posicion en el atril
		puestas=puestas.clear()
	else:          #saca solo la ficha seleccionada
		window[event].update(image_filename=tableroI[event])  					            #Pongo en donde estaba la ficha, la imagen del tablero original sin nada
		l=list(filter(lambda x:x[1]==puestas[event],list(originales.items())))[0][0]  		#Busco en el dict originales, cual de las fichas del atril, tenia la letra que puse en el tablero, y en l queda la key de la ficha, por ejemplo 'u2'
		window[l].update(image_filename=puestas[event])   									#Pongo en el atril la ficha en la interfaz
		letras[l]=puestas[event]    														#Vuelvo a poner en el dict de letras la letra segun corresponda a su posicion en el atril
		puestas=puestas.pop(event)          												#sacas la letra de las que pusiste en el tablero, ya que no esta mas
def colocarFicha(tableroI,tableroF,letras, window, colores,coordPlay):
	originales=letras.copy()  #Fichas del atril que tenia en el comienzo de la jugada
	puestas=dict()            #Fichas que voy poniendo en el tablero en esa jugada
	poner=False				  #Poner va a ser True cuando tenga una letra en mano para poner en el tablero
	letra=''		          #No tengo ninguna letra en mano, lo inicializo en ''
	direc='definir'
	nro=0						#Nro de ficha que esta poniendo
	event,_= window.read()
	salir=False
	valor=0
	while not event in (None,'Exit') and (salir==False):
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
				if(tableroF=={} and puestas=={}):            							#Si es la primera ficha de toda la partida entonces la puedo poner solo en UN lugar
					if(event==coordPlay):
						poner=ponerFicha(window, letra, puestas, event)   #Llamo al metodo ponerFicha que actualiza en el tablero la letra
						nro=nro+1    												#Sumo +1 porq agregue una ficha al tablero
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
						poner=ponerFicha(window, letra, puestas, ficha)    		#La coloco en el tablero segun la ficha que use 
						nro=nro+1
						letra=''
			else:                            
				if((event in puestas) and (event==ficha)):        													#Si no tengo una ficha en mano, pero toco una ficha colocada en el tablero
					s1=sg.popup_yes_no('Quiere sacar la ficha?')
					if(s1=='Yes'):    														#Si quiero sacar la ficha
						sacarFicha(tableroI, puestas, originales,letras, event, window)
						if(direc=='izq'):      																#la pos del tablero en donde podes poner va a ser -1 ya que en donde estaba la ficha ya no esta
							ficha=(ficha[0],ficha[1]-1)
						elif(direc=='abajo'):
							ficha=(ficha[0]-1,ficha[1])
						nro=nro-1																			#Como saco una ficha, el nro de ficha puesto es -1, de esta forma puedo volver a elegir la direccion si saco la 2da ficha de la palabra y si saco la primera ficha, poder seguir poniendo fichas(Si saco la primera y nro es >2 va  asuponer que hay una direccion o que habia una ficha previa puesta con la cual calcularla)
				elif(not event in (tableroF, puestas)):      												#Si no tenes una letra en mano y estas tocando un lugar en donde no hay nada
					sg.popup('No ha seleccionado una ficha para colocar')
		elif(event=='sacar'):
			s2=sg.popup_yes_no('Quiere sacar todas las fichas?')
			if(s2=='Yes'): 
				sacarFicha(tableroI, puestas, originales, letras, event, window)
				nro=0
		event,_= window.read()
		if(event=='palabra'):                                                     #Si toco el boton 'palabra', entonces significa que analizo si existe o no lo que forme en el tablero
			if(funciones.tipoPalabra(puestas)!="no_existe"):                      #llamo a la funcion tipoPalabra() que me dice si es un sustantivo, adjetivo, verbo o no existe en pattern
				valor = funciones.calcularPuntaje(puestas, tableroI, bolsa)       #calculo el puntaje segun las casillas y el valor de cada letra
				for x in puestas:                                  
					tableroF[x]=puestas[x]                     #agrego las fichas que se confirmaron forman una palbra en el diccionario de toda las fichas del juego, no de solo esa partida
				salir=True
			else:
				sg.popup('No existe esa palabra, vuelva a intentarlo')
				sacarFicha(tableroI, puestas, originales, letras, 'sacar', window)     #saco todas las fichas porque esa palabra no existe, no termina la jugada, vuelvo a intentar
		elif(event=='intercambiar'):   #Si intento intercambiar fichas durante la jugada, tienen que estar todas las fichas en el atril, no puede haber puestas. UNa vez que saque todas puedo hacer el intercambio y vuelvo a empezar a colocar
			if(puestas=={}):
				salir=True
			else:
				sg.popup('Para hacer un intercambio no puede haber fichas colocadas en el tablero de la jugada actual, saquelas para poder hacerlo, pero perdera el turno')
	return event, puestas, valor