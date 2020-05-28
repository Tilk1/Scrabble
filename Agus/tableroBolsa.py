import funciones
import PySimpleGUI as sg
import random
sg.theme('LightGray1')  # please make your windows colorful

def repartir(letras, bolsa, window):
	for x in letras:
		print(x)
		if(letras[x]==''):
			otro=True
			while(otro):
				letra=random.choice(list(bolsa))
				if(bolsa[letra]['cant']>0):
					otro=False
			if(x.find('u')):
				window[x].update(image_filename=letra)
			letras[x]=letra

tablero = []      ########GENERA TABLERO#######
for x in range(10):
	row = []
	for y in range(10):
		row.append(sg.RButton('',image_filename='vacio.png',image_size=(50, 50),size=(50,50),pad=(0,0),key= (x,y))) ##el filename no funciona
	tablero.append(row)

bolsa={'A.png':{'cant':11,'valor':1}, 'B.png':{'cant':11,'valor':3}, 'C.png':{'cant':8,'valor':1},'D.png':{'cant':7,'valor':1}, 'E.png':{'cant':7,'valor':1}, 'F.png':{'cant':7,'valor':1}, 'G.png':{'cant':7,'valor':1}, 'H.png':{'cant':5,'valor':1}, 'I.png':{'cant':7,'valor':1}, 'J.png':{'cant':7,'valor':1}, 'K.png':{'cant':7,'valor':1}, 'L.png':{'cant':7,'valor':1},'M.png':{'cant':7,'valor':1},'N.png':{'cant':7,'valor':1},'Ñ.png':{'cant':7,'valor':1},'O.png':{'cant':7,'valor':1},'P.png':{'cant':7,'valor':1},'Q.png':{'cant':7,'valor':1},'R.png':{'cant':7,'valor':1},'S.png':{'cant':7,'valor':1},'T.png':{'cant':7,'valor':1},'U.png':{'cant':7,'valor':1},'V.png':{'cant':7,'valor':1},'W.png':{'cant':7,'valor':1},'X.png':{'cant':7,'valor':1},'Y.png':{'cant':7,'valor':1},'Z.png':{'cant':7,'valor':1},'LL.png':{'cant':7,'valor':1},'RR.png':{'cant':7,'valor':1}}
letrasU={'u0':'', 'u1':'','u2':'','u3':'','u4':'','u5':'','u6':''}
letrasM={'m0':'', 'm1':'','m2':'','m3':'','m4':'','m5':'','m6':''}
layout = [
		  [sg.Text('ma'),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='m0',size=(50,50)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='m1', size=(4,2)),sg.Button('',image_filename='color3.png',image_size=(50, 50),key='m2', size=(4,2)),sg.Button('',image_filename='color4.png',image_size=(50, 50),key='m3', size=(4,2)),sg.Button('',image_filename='color5.png',image_size=(50, 50),key='m4', size=(4,2)),sg.Button('',image_filename='color1.png',image_size=(50, 50),key='m5',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='m6', size=(4,2))],
		  [sg.Image(filename= '',key='image')],
		  [sg.Column(tablero),sg.Button('COMENZAR')], ##tablero aca
		  [sg.Text('us'),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='u0',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='u1', size=(4,2)),sg.Button('',image_filename='color3.png',image_size=(50, 50), key='u2', size=(4,2)),sg.Button('',image_filename='color4.png',image_size=(50, 50), key='u3', size=(4,2)),sg.Button('',image_filename='color5.png',image_size=(50, 50), key='u4', size=(4,2)),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='u5',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50), key='u6', size=(4,2))],
		  [ sg.Button('Exit'), sg.Button('palabra')]
		  ]

colores= ['color1.png','color2.png','color3.png','color4.png','color5.png',]
window = sg.Window('tablero', layout)
event, values = window.read()

repartir(letrasU,bolsa, window)
repartir(letrasM,bolsa, window)

while True:
	event, values = window.read()
	print(event, values)
	if event in ('u0', 'u1','u2','u3','u4','u5','u6'):
		letra=letrasU[event]
		print(letra)
		window[event].update(image_filename=random.choice(colores))
		letrasU[event]=''
		event, values = window.read()
		window[event].update(image_filename=letra)
	elif(event=='palabra'):
		repartir(letrasU, bolsa, window)
	if event in (None, 'Exit'):
		break 	
window.close()