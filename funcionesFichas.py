import random
import PySimpleGUI as sg
import funciones
import os
cwd = os.getcwd()

def randomLetra(bolsa):   #elige una letra random de la bolsa y la quita d ela bolsa
	"""
    Elige una letra de forma aleatoria y le descuenta en su cant 1. Cuando la cantidad de una letra llega a 0 se eleimina de la bolsa
	Cuando la bolsa se vacia, se retorna vacio para indicar la finalizacion del juego.

    """
	if(bolsa=={}):
		return 'vacio'
	else:
		otro = True
		while(otro):
			letra = random.choice(list(bolsa))   #elijo aleatoriamente una letra
			if(bolsa[letra]['cant'] > 0):   #me fijo si hay suficientes de esa letra para usar en la bolsa
				otro = False
				bolsa[letra]['cant'] = bolsa[letra]['cant']-1   #descuento 1 a la cant de letras ya que la saco de la bolsa
				if(bolsa[letra]['cant'] == 0):
					del(bolsa[letra])
		return letra

def repartir(letras, bolsa, window):   #reparte las fichas al principio del juego y de cada jugada si faltan fichas
	"""
    Reparto fichas al usuario y a la maquina. Si esta vacia la bolsa directamente devuelvo vacio. En caso de contener letras
	Repongo una letra en cada lugar del atril que no tenga una letra, cuando no tiene una letra en el atril va a estar guardado como
	letra='', entonces va a recorrer el atril y usando la funcion randomLetra voy a reponer las que faltan.
	Al inicio del juego se van a reponer las 7.
	Retorno sigo cuando la bolsa sigue con letras, no finaliza el juego.

    """
	if(bolsa=={}):
		return 'vacio'
	else:
		x=0
		letra=''
		q=list(letras.keys())[0].split('0')[0]   #me dice si es usuario o maquina
		while(letra!='vacio' and x<=6):
			if(letras[q+str(x)]==''):    #Tengo en cuenta letras[x]=='' ya que al principio del juego, el diccionario letras es letrasU={'u0':'', 'u1':'','u2':'','u3':'','u4':'','u5':'','u6':''} y cuando no hay ninguna letra en el atril en esa pos
				letra=randomLetra(bolsa)
				if(letra!='vacio'):
					if(q=='u'):  #corroboro que no es la maquina, ya que las fichas de la maquina tienen que estar boca abajo y no mostar la letra, entonces en la interfaz no se actualizaria la imagen
						window[q+str(x)].update(image_filename=os.path.join(cwd,letra))
					letras[q+str(x)]=letra
			x=x+1
		if(letra!='vacio'):  #si mientras repartia me devolvió que la bolsa esta vacia, entonces va a devolver vacio y termina el juego
			return 'sigo'
		else:
			return 'vacio'

def sumarFicha(bolsa, copia, letra):
	"""
    Cuando hago un intercambio devuelvo las fichas a la bolsa. Cuando se devuelve a la bolsa una 
	letra que ya no existe(se eliminó previamnete debido a que cant llegó a 0) devo volver a crearla en el diccionario con
	su respectiva key. Este es el primer caso del if (bolsa.get(letra,0)==0).
	El segundo caso es que se devuelva a la bolsa una letra qu sigue existiendo en esta, por lo que simplemente se accede a
	ella y se suma. Este es el caso del else.

    """
	print('devuelvo a la bolsa: ',letra)
	if(bolsa.get(letra,0)==0):
		bolsa[letra]=copia[letra]   #creo la letra con su valor y cant en 1 
		bolsa[letra]['cant']=1
	else:
		bolsa[letra]['cant']=bolsa[letra]['cant']+1  #sumo 1 a la bolsa de esa letra

def intercambiarFichas(letras, bolsa, copia, window, cant):
	"""
    Intercambiar ficha. Cuando se intercambian las 7 fichas se entra a if(cant==7), no se pide al usuario que elija cuales quiere cambiar ya que
	son todas. Cuando la cantidad es menor a 7, el usuario elige cuales letras quiere intercambiar.
	La máquina usa también la función cuando no puede formar palabras después de repetidos intentos, entonces cambia todas las fichas
	del atril.

    """
	if(bolsa=={}):
		sg.popup('No quedan mas fichas en la bolsa, no se ha podido realizar el intercambio')
	else:
		letra=''
		x=0
		q=list(letras.keys())[0].split('0')[0]  #se fija si es la maquina o el usuario
		if(cant==7):                                          #cuando quiero intercambiar todas se hace automaticamentr y no elijo cuales de a una
			while(letra!='vacio' and x<=6):
				letra=randomLetra(bolsa)
				if(letra!='vacio'):
					print('intercambio la ficha',letra, 'de ',q+str(x))  
					if(q=='u'): 
						window[q+str(x)].update(image_filename=os.path.join(cwd,letra))  #actualiza solamente el atril del usuario, las fichas de de la maquina estan dadas vueltas
					sumarFicha(bolsa, copia, letras[q+str(x)])  #agrego la letra que intercambie a la bolsa
					letras[q+str(x)]=letra
					x=x+1  #voy al siguiente indice del atril
		else:
			cambios=list()    #no me deja intercambiar una letra que ya intercambie en ese momento
			while(x<cant and letra!='vacio'):
				sigo=True
				while(sigo):      #En el caso de que el evento no sea algunas de las fichas del atril para cambiarla, entonces sigue pidiendo que se elija y no hace nada
					event,_=window.read()
					if (not event in cambios) and (event in ('u0', 'u1','u2','u3','u4','u5','u6')):  #se queda esperando que el usuario elija que letras intercambiar
						letra=randomLetra(bolsa)
						cambios.append(event)
						if(letra!='vacio'):
							print('intercambio la ficha',letra)
							print(event)
							window[event].update(image_filename=os.path.join(cwd,letra))
							sumarFicha(bolsa, copia, letras[event])
							letras[event]=letra
							x=x+1
						sigo=False
		if(letra=='vacio'):
			sg.popup('No quedan mas fichas en la bolsa, se han intercambiado las posibles')
		elif(q=='u'):   
			sg.popup('Intercambio realizado!')


def ponerFicha(window,letra, puestas, event):
	"""
    Coloca la ficha en el tablero. Actualiza la imagen en el tablero de la letra que se coloca.

    """
	window[event].update(image_filename=os.path.join(cwd,letra))
	puestas[event]=letra
	return False

def sacarFicha(tableroI, puestas, originales, letras, event, window):
	"""
    Función que saca las fichas, cuando el evento es igual a sacar, saco todas las fichas, letras[x] son las que tiene en el atril, 
	las vuelvo a poner en el original. Puestas tiene las letras puestas en esa jugada en el tablero. Se eliminan todas, ya que se sacan.
	En caso de sacar solo una ficha individual, de Puestas  solo se saca la ficha individual y se actualiza el tablero.

    """
	if(event=='sacar'):     #saco todas las fichas
		for y in puestas:
			for x in originales:
				if (originales[x]==puestas[y]):
					window[y].update(image_filename=os.path.join(cwd,tableroI[y]))							#Pongo en donde estaba la ficha, la imagen del tablero original sin nada
					window[x].update(image_filename=os.path.join(cwd,originales[x]))							#Pongo en el atril la ficha en la interfaz
					letras[x]=originales[x]    												#Vuelvo a poner en el dict de letras la letra segun corresponda a su posicion en el atril
		puestas=puestas.clear()
	else:          #saca solo la ficha seleccionada
		window[event].update(image_filename=os.path.join(cwd,tableroI[event]))  					            #Pongo en donde estaba la ficha, la imagen del tablero original sin nada
		l=list(filter(lambda x:x[1]==puestas[event],list(originales.items())))[0][0]  		#Busco en el dict originales, cual de las fichas del atril, tenia la letra que puse en el tablero, y en l queda la key de la ficha, por ejemplo 'u2'
		window[l].update(image_filename=os.path.join(cwd,puestas[event]))   									#Pongo en el atril la ficha en la interfaz
		letras[l]=puestas[event]    														#Vuelvo a poner en el dict de letras la letra segun corresponda a su posicion en el atril
		puestas=puestas.pop(event)          												#sacas la letra de las que pusiste en el tablero, ya que no esta mas

def colocarFicha(inter,tableroI,tableroF,letras, window, colores,coordPlay, bolsa, puestas, palpos):
	"""
    Tiene en cuenta todo el proceso de colocar fichas del usuario. Se tiene en cuenta que al tocar un indice del atril, el uduario puede estar queriendo 
	seleccionar una ficha para colocarla en el tablero o tiene una en mano y se arrepintió, por lo que quiere devolverla.
	Cuando el evento es una coordenada del tablero, el usuario puede estar queriendo colocar una ficha, en ese caso se tiene 
	que asegurar que no hay una ficha puesta de jugadas anteriores o de esta misma. O puede estar queriendo seleccionar una ficha
	ya puesta en el tablero y sacarla.
	También se tiene que tener en cuenta que pase la primer palabra por el incio.
	Se calcula si la palabra es válida según configuración y el pattern, se calcula el puntaje y se retora.
	A la hora de colocar las fichas solo se admite que sean horizontales de izquierda a derecha o verticales de arriba hacia abajo.
	La primer ficha de la palabra puede colocarse en cualquier lado, la segunda ficha determina la dirección de la palabra, es decir, si 
	es hacia la derecha(horizontal) o hacia abajo(vertical), y las siguientes letras solo van a poder colocarse teniendo en
	cuenta esa dirección.
	Cuando se presiona intercambiar, sale de la función y pierde el turno.

    """
	originales=letras.copy()  #Fichas del atril que tenia en el comienzo de la jugada
	#puestas=dict()            #Fichas que voy poniendo en el tablero en esa jugada
	poner=False				  #Poner va a ser True cuando tenga una letra en mano para poner en el tablero
	letra=''		          #No tengo ninguna letra en mano, lo inicializo en ''
	direc='definir'
	nro=0						#Nro de ficha que esta poniendo
	salir=False
	valor=0	
	event,_= window.read()
	while not event in (None,'exit','posponer') and (salir==False):
		if event in ('u0', 'u1','u2','u3','u4','u5','u6'):  				#Si selecciono una letra
			if ((letras[event]=='') and (originales[event]==letra)):  #Si en el diccionario letras que guarda la imagen actual de la ficha no hay una letra(=''), pero lo estoy selecionando, significa que quiero volver a poner la letra en su lugar(si es que tengo un aletra en mano, letra!=''). originales[event]==letra----corrobora que se quiere poner en la misma pos en el atril
				window[event].update(image_filename=os.path.join(cwd,letra))					 #originales[event]==letra corrobora que la estoy poniendo en la misma pos original. Hago un update de la ficha en la interfaz con la letra
				letras[event]=letra
				letra=''   													#Como no tengo ninguna letra en mano, la pongo en ''
			elif((letras[event]!='') and (letra=='')):   #Si la ficha tiene una aletra y no tinen un color(=''), y no tengo ninguna letra en mano(corroboro esto asi no la pierdo en caso de haber agarrado una y no haber hecho nada con ella), entonces la agarro
				letra=letras[event]   								#letra la actualizo con la de la ficha
				color=random.choice(colores)   						#pongo un color en la ficha que agarre, "queda vacia"
				window[event].update(image_filename=os.path.join(cwd,color))
				letras[event]=''    								#en el diccionario donde tengo las imag de las fichas pongo que tengo un color
				poner=True
		elif(isinstance(event, tuple)):    							#Si toco el tablero
			if(poner and letra!=''):    							#Si tengo una ficha en mano (poner=True) y (letra!='')
				if(event in tableroF):    													#Si estoy intentando poner la ficha arriba de una de otra partida
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
		elif(event=='intercambiar'):   #Si intento intercambiar fichas durante la jugada, tienen que estar todas las fichas en el atril, no puede haber puestas. UNa vez que saque todas puedo hacer el intercambio y vuelvo a empezar a colocar
			if(inter>=3):
				sg.popup('el numero máximo de intercambios es 3, ha llegado al límite')
			else:
				if(puestas=={}):
					salir=True
				else:
					sg.popup('Para hacer un intercambio no puede haber fichas colocadas en el tablero de la jugada actual, saquelas para poder hacerlo, pero perdera el turno')		
		elif(event=='palabra'):                                                     #Si toco el boton 'palabra', entonces significa que analizo si existe o no lo que forme en el tablero
			ponerpal=True
			if(tableroF=={}):
				if (not coordPlay in puestas.keys()):
					ponerpal=False
			if(ponerpal):
				tipoP=funciones.tipoPalabra(puestas)
				print(tipoP)
				print(palpos)
				if((tipoP!="no_existe") and (tipoP in (palpos))):                      #llamo a la funcion tipoPalabra() que me dice si es un sustantivo, adjetivo, verbo o no existe en pattern
					valor = funciones.calcularPuntaje(puestas, tableroI, bolsa)       #calculo el puntaje segun las casillas y el valor de cada letra
					for x in puestas:                                  
						tableroF[x]=puestas[x]                     #agrego las fichas que se confirmaron forman una palbra en el diccionario de toda las fichas del juego, no de solo esa partida
					salir=True
				else:
					sg.popup('No existe esa palabra, vuelva a intentarlo')
					sacarFicha(tableroI, puestas, originales, letras, 'sacar', window)     #saco todas las fichas porque esa palabra no existe, no termina la jugada, vuelvo a intentar
					nro=0
			else:
				sg.popup('La primera palabra del juego debe pasar por el inicio')
				sacarFicha(tableroI, puestas, originales, letras, 'sacar', window)     #saco todas las fichas porque esa palabra no existe, no termina la jugada, vuelvo a intentar
				nro=0
		if(salir!=True):   
			event,_= window.read()
	return event, valor