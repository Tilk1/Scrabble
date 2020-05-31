def crearTablero(tab,fila, column, imagenes,sg):
	tablero = []
	for x in range(fila):
		row = []
		for y in range(column):
			if((x,y) in tab['letraDoble']):
				im=tab['letraDoble'][0]
			elif((x,y) in tab['letraTriple']):
				im=tab['letraTriple'][0]
			elif((x,y) in tab['palabraDoble']):
				im=tab['palabraDoble'][0]
			elif((x,y) in tab['descuento2']):
				im=tab['descuento2'][0]
			elif((x,y) in tab['descuento1']):
				im=tab['descuento1'][0]
			elif((x,y) in tab['descuento3']):
				im=tab['descuento3'][0]
			elif((x,y) in tab['palabraTriple']):
				im=tab['palabraTriple'][0]
			elif((x,y)==(7,7)):
				im='play.png'
			else:
				im='vacio1.png'
			imagenes[(x,y)]=im
			row.append(sg.Button('',image_filename=im,border_width=0,image_size=(46, 46),pad=(0,0),key=(x,y)))
		tablero.append(row)
	return tablero

tablero1={'letraDoble':['vacio.png',(0,1),(0,7),(0,13),(8,3),(8,11),(11,6),(11,8),(3,6),(3,8),(9,4),(9,10),(10,5),(10,9),(4,5),(4,9),(5,4),(5,10),(6,3),(6,11),(14,1),(14,7),(14,13)],'letraTriple':['vacio2.png',(0,5),(0,9),(3,2),(3,12),(4,1),(4,13),(5,0),(5,14),(5,6),(5,8),(9,0),(9,14),(9,6),(9,8),(10,1),(10,13),(11,2),(11,12),(14,5),(14,9)],'palabraDoble':['vacio6.png',(1,1),(1,13),(3,5),(3,9),(5,3),(5,11),(9,3),(9,11),(11,5),(11,9),(13,1),(13,13)],'descuento2':['vacio4.png',(7,1),(7,13),(10,6),(10,8)],'descuento1':['vacio3.png',(1,0),(1,14),(4,6),(4,8),(7,4),(7,10),(13,0),(13,14)],'descuento3':['vacio5.png',(2,3),(2,11),(12,3),(12,11)],'palabraTriple':['vacio7.png',(0,4),(0,10),(7,0),(7,14),(14,4),(14,10)]}

