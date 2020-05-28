import PySimpleGUI as sg
from random import randint

MAX_ROWS = MAX_COL = 10

tablero= [[sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
espacio=[[sg.Text(' ')]]
letras=[[sg.Button('A', size=(4,2)),sg.Button('B', size=(4,2)),sg.Button('C', size=(4,2)),sg.Button('D', size=(4,2))]]
layout = tablero+espacio+letras

window = sg.Window('Minesweeper', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    window[event].update('A')   # To change a button's text, use this pattern
    # For this example, change the text of the button to the board's value and turn color black
    #window[event].update(board[event[0]][event[1]], button_color=('white','black'))
window.close()