import sys
import random
 
import PySimpleGUI as sg
mode = "tkinter"
mysize = (2,1)
BAR_WIDTH = 100
BAR_SPACING = 90
EDGE_OFFSET = 3
GRAPH_SIZE = (300,2000)
DATA_SIZE = (800,500)
 
bcols = ['blue','red','green','blue','red','green','blue','red','green','green']
myfont = "Ariel 18"
 
graph = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)

 
layout = [[sg.Text('Pi Sensor Values',font=myfont)],
  [graph],
#   [sg.Text('1',text_color=bcols[0],font=myfont,size= mysize ),
#   sg.Text('2',text_color=bcols[1],font=myfont,size= mysize ),
#   sg.Text('3',text_color=bcols[2],font=myfont,size= mysize),
#   sg.Text('4',text_color=bcols[2],font=myfont,size= mysize),
#   sg.Text('5',text_color=bcols[2],font=myfont,size= mysize),
#   sg.Text('6',text_color=bcols[2],font=myfont,size= mysize),
#   sg.Text('7',text_color=bcols[2],font=myfont,size= mysize),
#   sg.Text('8',text_color=bcols[2],font=myfont,size= mysize),
#   sg.Text('9',text_color=bcols[2],font=myfont,size= mysize),
#   sg.Text('10',text_color=bcols[2],font=myfont,size= mysize)],
  [sg.Exit()]]
 
window = sg.Window('Real Time Charts', layout)
while True:
    event, values = window.read(timeout=2000)
    if event in (None, 'Exit'):
        break
 
    graph.erase()
    for i in range(10):
# Random value are used. Add interface to Pi sensors here:
        graph_value = random.randint(0, 400)
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
        bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color=bcols[i])
        #<span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>graph.draw_text(text=str(graph_value), location=(i*BAR_SPACING+EDGE_OFFSET+15, graph_value+10),color=bcols[i],font=myfont)
 
window.close()