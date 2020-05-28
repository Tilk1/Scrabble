import PySimpleGUI as sg
import random

def repartir(letras, bolsa, cant, quien):
	if(quien=='usuario'):
		event='u'
	else:
		event='m'
	for x in letras:
		while(otro):
			letra=random.randrange(bolsa)
			if(bolsa[letra]['cant']>0):
				otro=False
		#window[event+].update(letra)

MAX_ROWS = MAX_COL = 10

bolsa={'A':{'cant':11,'valor':1}, 'B':{'cant':11,'valor':3}, 'C':{'cant':8,'valor':1},'D':{'cant':7,'valor':1}, 'E':{'cant':7,'valor':1}, 'F':{'cant':7,'valor':1}, 'G':{'cant':7,'valor':1}, 'H':{'cant':5,'valor':1}, 'I':{'cant':7,'valor':1}, 'J':{'cant':7,'valor':1}, 'K':{'cant':7,'valor':1}, 'L':{'cant':7,'valor':1},'M':{'cant':7,'valor':1},'N':{'cant':7,'valor':1},'Ñ':{'cant':7,'valor':1},'O':{'cant':7,'valor':1},'P':{'cant':7,'valor':1},'Q':{'cant':7,'valor':1},'R':{'cant':7,'valor':1},'S':{'cant':7,'valor':1},'T':{'cant':7,'valor':1},'U':{'cant':7,'valor':1},'V':{'cant':7,'valor':1},'W':{'cant':7,'valor':1},'X':{'cant':7,'valor':1},'Y':{'cant':7,'valor':1},'Z':{'cant':7,'valor':1}}

tablero= [[sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
espacio=[[sg.Text(' ')]]
usuario=[[sg.Text('  '),sg.Button('', key='u0',size=(4,2)),sg.Button('',key='u1', size=(4,2)),sg.Button('',key='u2', size=(4,2)),sg.Button('',key='u3', size=(4,2)),sg.Button('',key='u4', size=(4,2)),sg.Button('',key='u5',size=(4,2)),sg.Button('',key='u6', size=(4,2))]]
maquina=[[sg.Text('  '),sg.Button('', key='m0',size=(4,2)),sg.Button('',key='m1', size=(4,2)),sg.Button('',key='m2', size=(4,2)),sg.Button('',key='m3', size=(4,2)),sg.Button('',key='m4', size=(4,2)),sg.Button('',key='m5',size=(4,2)),sg.Button('',key='m6', size=(4,2))]]
layout = maquina+[[sg.Text(' ')]]+tablero+[[sg.Text(' ')]]+usuario
		
window = sg.Window('tablero', layout)

while True:
	event, values = window.read()
	print(event, values)
	if event in (None, 'Exit'):
		break
	window[event].update('A') 
window.close()
#alalalalala
#aaaaaaaaaaaaaaaaaaaaaaaa