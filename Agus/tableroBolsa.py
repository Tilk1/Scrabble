import funciones
import PySimpleGUI as sg
import random
sg.theme('LightGrey1')  # please make your windows colorful

def repartir(letras, bolsa, window):
	for x in letras:
		if(letras[x]==''):
			otro=True
			while(otro):
				letra=random.choice(list(bolsa))
				if(bolsa[letra]['cant']>0):
					otro=False
			window[x].update(letra)
			letras[x]=letra

tablero = []      ########GENERA TABLERO#######
for x in range(10):
	row = []
	for y in range(10):
		row.append(sg.RButton('',size=(4,2),pad=(0,0),key= (x,y))) ##el filename no funciona
	tablero.append(row)

bolsa={'A':{'cant':11,'valor':1}, 'B':{'cant':11,'valor':3}, 'C':{'cant':8,'valor':1},'D':{'cant':7,'valor':1}, 'E':{'cant':7,'valor':1}, 'F':{'cant':7,'valor':1}, 'G':{'cant':7,'valor':1}, 'H':{'cant':5,'valor':1}, 'I':{'cant':7,'valor':1}, 'J':{'cant':7,'valor':1}, 'K':{'cant':7,'valor':1}, 'L':{'cant':7,'valor':1},'M':{'cant':7,'valor':1},'N':{'cant':7,'valor':1},'Ñ':{'cant':7,'valor':1},'O':{'cant':7,'valor':1},'P':{'cant':7,'valor':1},'Q':{'cant':7,'valor':1},'R':{'cant':7,'valor':1},'S':{'cant':7,'valor':1},'T':{'cant':7,'valor':1},'U':{'cant':7,'valor':1},'V':{'cant':7,'valor':1},'W':{'cant':7,'valor':1},'X':{'cant':7,'valor':1},'Y':{'cant':7,'valor':1},'Z':{'cant':7,'valor':1}}
letrasU={'u0':'', 'u1':'','u2':'','u3':'','u4':'','u5':'','u6':''}
letrasM={'m0':'', 'm1':'','m2':'','m3':'','m4':'','m5':'','m6':''}
layout = [[sg.Text('Saber si existe la palabra:'), sg.Text(size=(12,1), key='-OUTPUT-'), sg.Button('Show'),],
		  [sg.Input(key='-IN-')],
		  [sg.Text('  '),sg.Button('', key='m0',size=(4,2)),sg.Button('',key='m1', size=(4,2)),sg.Button('',key='m2', size=(4,2)),sg.Button('',key='m3', size=(4,2)),sg.Button('',key='m4', size=(4,2)),sg.Button('',key='m5',size=(4,2)),sg.Button('',key='m6', size=(4,2))],
		  [sg.Image(filename= '',key='image')],
		  [sg.Button('COMENZAR'),sg.Column(tablero)], ##tablero aca
		  [sg.Text('  '),sg.Button('', key='u0',size=(4,2)),sg.Button('',key='u1', size=(4,2)),sg.Button('',key='u2', size=(4,2)),sg.Button('',key='u3', size=(4,2)),sg.Button('',key='u4', size=(4,2)),sg.Button('',key='u5',size=(4,2)),sg.Button('',key='u6', size=(4,2))],
		  [ sg.Button('Exit'), sg.Button('palabra')]
		  ]

window = sg.Window('tablero', layout)
event, values = window.read()

repartir(letrasU,bolsa, window)
repartir(letrasM,bolsa, window)

while True:
	event, values = window.read()
	print(event, values)
	if event in ('u0', 'u1','u2','u3','u4','u5','u6'):
		letra=letrasU[event]
		window[event].update('')
		letrasU[event]=''
		event, values = window.read()
		window[event].update(letra)
	elif(event=='palabra'):
		repartir(letrasU, bolsa, window)
	if event in (None, 'Exit'):
		break 	
window.close()