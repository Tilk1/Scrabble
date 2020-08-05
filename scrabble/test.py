import json
with open('posponer.txt','a+') as archivo: #lo abro en modo append ya que en caso de no existir el archivo, crea uno nuevo y no da error, y si existe, puedo agregar nuevos jugadores. 
	if(archivo.tell()>0):   #Me fijo si el archivo esta vacio, si ya se registraron usuarios entonces tengo que agregar al diccionario ya creado
		archivo.seek(0)     #voy al inicio del archivo para poder tomar los datos
		jugadores=json.load(archivo)
	else:
		jugadores=dict()      #Si todavia no hubo jugadores entonces creo el diccionario