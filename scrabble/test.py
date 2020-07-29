import PySimpleGUI as sg

val1 = {'A': 2, 'E': 2, 'O': 3, 'S': 3, 'I': 3, 'U': 3, 'N': 3, 'L': 9, 'R': 3, 'T': 3, 'C': 3, 'D': 3, 'G': 3, 'M': 4, 'B': 4, 'P': 4, 'F': 5, 'H': 5, 'V': 5, 'Y':5, 'J': 7, 'K': 9, 'Ñ': 9, 'Q': 9, 'RR': 9, 'W': 9, 'X': 9, 'Z': 11}

row1 = []
row2 = []
row3 = []
for x in val1.keys():
    row1.append(sg.Text(x+' ', font=('Fixedsys', 17)))
    row2.append(sg.Combo(values=[x for x in range(1, 21)],default_value=1, key='letV', font=('Fixedsys', 15), text_color='purple', background_color='white'))
    row3.append(sg.Combo(values=[x for x in range(1, 21)],default_value=1, key='cantidV', font=('Fixedsys', 15), text_color='purple', background_color='white'))
layout= [row1, row2, row3
]
window = sg.Window('tablero', layout)
event, values=window.read()