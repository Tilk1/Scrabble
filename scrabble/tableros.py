import os
cwd = os.getcwd()

def crearTablero(tab, fila, column, imagenes, sg):
	"""
    Crea una matriz con columnas y filas segun el tablero especifico. Segun la dimension de esta, las imagenes que va a 
	usar para cada coordenada.

    """
	tablero = []
	for x in range(fila):  # crea el tablero
		row = []
		for y in range(column):
			# dependiendo el tablero, las coordenadas van a tener una imagen particula
			if((x, y) in tab['letraDoble']):
				im = tab['letraDoble'][0]
			elif((x, y) in tab['letraTriple']):
				im = tab['letraTriple'][0]
			elif((x, y) in tab['palabraDoble']):
				im = tab['palabraDoble'][0]
			elif((x, y) in tab['descuento2']):
				im = tab['descuento2'][0]
			elif((x, y) in tab['descuento1']):
				im = tab['descuento1'][0]
			elif((x, y) in tab['descuento3']):
				im = tab['descuento3'][0]
			elif((x, y) in tab['palabraTriple']):
				im = tab['palabraTriple'][0]
			elif((x, y) in tab['play']):
				im = tab['play'][0]
			else:
				im = 'vacio.png'  # si no es una casilla especial
			imagenes[(x, y)] = im
			row.append(sg.Button('', image_filename=os.path.join(cwd,'imagenes',im), border_width=0, image_size=(
				46, 46), pad=(0, 0), key=(x, y)))  # agrega a la fila, la imagen en esa columna
		tablero.append(row)
	return tablero

#tableros, coordenadas y sus casillas

tablero1={'play':['play.png',(7,7)],'letraDoble':['lx2.png',(0,1),(0,7),(0,13),(8,3),(8,11),(11,6),(11,8),(3,6),(3,8),(9,4),(9,10),(10,5),(10,9),(4,5),(4,9),(5,4),(5,10),(6,3),(6,11),(14,1),(14,7),(14,13)],'letraTriple':['lx3.png',(0,5),(0,9),(3,2),(3,12),(4,1),(4,13),(5,0),(5,14),(5,6),(5,8),(9,0),(9,14),(9,6),(9,8),(10,1),(10,13),(11,2),(11,12),(14,5),(14,9)],'palabraDoble':['px2.png',(1,1),(1,13),(3,5),(3,9),(5,3),(5,11),(9,3),(9,11),(11,5),(11,9),(13,1),(13,13)],'descuento2':['-2.png',(7,1),(7,13),(10,6),(10,8)],'descuento1':['-1.png',(1,0),(1,14),(4,6),(4,8),(7,4),(7,10),(13,0),(13,14)],'descuento3':['-3.png',(2,3),(2,11),(12,3),(12,11)],'palabraTriple':['px3.png',(0,4),(0,10),(7,0),(7,14),(14,4),(14,10)]}
tablero3={'play':['play.png',(7,10)],'letraDoble':['lx2.png',(1,1),(2,2),(3,3),(4,4),(13,1),(12,2),(11,3),(10,4),(1,18),(2,17),(3,16),(4,15),(13,18),(12,17),(11,16),(10,15)],'letraTriple':['lx3.png',(1,7),(1,12),(6,11),(8,9),(13,7),(13,12),(5,5),(9,5),(5,14),(9,14)],'palabraDoble':['px2.png',(7,0),(3,9),(6,6),(8,6),(11,9),(6,13),(8,13),(7,19)],'descuento2':['-2.png',(2,8),(2,11),(6,2),(6,9),(6,17),(8,2),(8,11),(8,17),(12,8),(12,11)],'descuento1':['-1.png',(0,9),(3,10),(7,3),(7,16),(11,10),(14,9)],'descuento3':['-3.png',(4,0),(5,1),(9,1),(10,0),(0,6),(0,13),(14,6),(14,13),(4,19),(5,18),(9,18),(10,19)],'palabraTriple':['px3.png',(0,0),(14,0),(14,10),(7,7),(14,19),(0,19),(0,10),(7,12)]}
tablero2={'play':['play.png',(7,8)],'palabraDoble':['px2.png',(7,6),(11,1),(3,1),(5,8),(9,8),(3,15),(11,15),(7,10)],'letraTriple':['lx3.png',(14,4),(14,13),(11,6),(11,11),(3,6),(3,11),(0,4),(0,13)],'letraDoble':['lx2.png',(13,1),(12,2),(11,3),(10,4),(9,5),(5,5),(4,4),(3,3),(2,2),(1,1),(13,15),(12,14),(11,13),(10,12),(9,11),(5,11),(4,12),(3,13),(2,14),(1,15)],'descuento2':['-2.png',(9,2),(5,2),(3,8),(11,8),(5,14),(9,14)],'descuento1':['-1.png',(13,5),(13,12),(9,6),(7,4),(5,6),(1,5),(9,10),(5,10),(7,12),(1,12)],'descuento3':['-3.png',(7,2),(1,8),(13,8),(7,14)],'palabraTriple':['px3.png',(0,0),(7,0),(14,0),(14,8),(0,8),(0,16),(7,16),(14,16),(8,7),(6,7),(6,9),(8,9)]}