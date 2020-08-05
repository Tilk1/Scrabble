import json
#with open('posponer.txt','a+') as archivo: #lo abro en modo append ya que en caso de no existir el archivo, crea uno nuevo y no da error, y si existe, puedo agregar nuevos jugadores. 
	#if(archivo.tell()>0):   #Me fijo si el archivo esta vacio, si ya se registraron usuarios entonces tengo que agregar al diccionario ya creado
	#	archivo.seek(0)     #voy al inicio del archivo para poder tomar los datos
	#	jugadores=json.load(archivo)
	#else:
	#	jugadores=dict()      #Si todavia no hubo jugadores entonces creo el diccionario
bolsa = {'A.png': {'cant': 0, 'valor': 0},
			'B.png': {'cant': 0, 'valor': 0},
			'C.png': {'cant': 0, 'valor': 0},
			'D.png': {'cant': 0, 'valor': 0},
			'E.png': {'cant': 0, 'valor': 0},
			'F.png': {'cant': 0, 'valor': 0},
			'G.png': {'cant': 0, 'valor': 0},
			'H.png': {'cant': 0, 'valor': 0},
			'I.png': {'cant': 7, 'valor': 1},
			'J.png': {'cant': 7, 'valor': 1},
			'K.png': {'cant': 7, 'valor': 1},
			'L.png': {'cant': 7, 'valor': 1},
			'M.png': {'cant': 7, 'valor': 1},
			'N.png': {'cant': 7, 'valor': 1},
			'Ñ.png': {'cant': 7, 'valor': 1},
			'O.png': {'cant': 7, 'valor': 1},
			'P.png': {'cant': 7, 'valor': 1},
			'Q.png': {'cant': 7, 'valor': 1},
			'R.png': {'cant': 7, 'valor': 1},
			'S.png': {'cant': 7, 'valor': 1},
			'T.png': {'cant': 7, 'valor': 1},
			'U.png': {'cant': 7, 'valor': 1},
			'V.png': {'cant': 7, 'valor': 1},
			'W.png': {'cant': 7, 'valor': 1},
			'X.png': {'cant': 7, 'valor': 1},
			'Y.png': {'cant': 7, 'valor': 1},
			'Z.png': {'cant': 7, 'valor': 1},
			'LL.png': {'cant': 7, 'valor': 1},
			'RR.png': {'cant': 7, 'valor': 1}}
datos={'bolsa':[bolsa]}
print(datos)