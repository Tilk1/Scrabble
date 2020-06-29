# ScrabblleUNLPAgusSanti
![](https://i.imgur.com/O7vRM8o.png)


## Requisitos

Python 3.6.8

PySimpleGUI (Libreria)

Pattern (Libreria)

## Instrucciones

Se debe ejecutar el archivo SrabbleAR.py dentro del directorio scrabble para comenzar el juego. Se mostrará una ventana de inicio del juego, que muestra el nivel en el que se esta jugando y se puede cambiar a facil, dificil y medio, o se pueden configurar los detalles del nivel con el boton 'configuracion'(actualmente no funciona, solo se ve en la interfaz, al igual que el botón top10). Se debe presionar el boton 'jugar' para mostar el tablero. 
Para comenzar la partida se debe tocar 'iniciar'. Todavia no se configuró el funcionamiento de la IA, por lo que siempre es el turno del usuario, y el tiempo no se tiene en cuenta.
Para intercambiar las letras se toca el botón 'intercambiar', para sacar todas las fichas colocadas en esa jugada del tablero se toca el botón 'sacar todas' y para que se tenga en cuenta la palabra formada con las fichas se usa el botón 'palabra'. 
Se reparten las fichas al iniciarse la jugada, al colocar las fichas en el tablero estas se pueden quitar individualmente tocando sobre la ultima colocada, en caso de querer sacar todas se usa el botón 'sacar todas' como antes dicho. En el caso de tener una ficha en mano y arrepentirse de colocarla en el tablero, si se presiona la posición de la ficha en donde estaba en el átril, esta vuelve a donde estaba. 

## Notas adicionales

El archivo funciones.py contiene funciones varias relacionadas al analisis de la palabra formada y su puntaje. El archivo funcionesFichas.py tiene funciones relacionadas al manejo de las fichas como colocarFicha, SacarFicha, Repartir, entre otras. El archivo tableros.py tine los tableros disponibles y una funcion para crear el tablero.
Actualmente se usa un tablero de 15x15 pero uno de 15x20 tambien esta disponible, se tiene que modificar el código del archivo SrabbleAR.py para hacerlo, ya que todavia no se puede configurar desde la interfaz.

## Participantes

Maria Agustina Gonzalez y Santiago Jose Lizondo Colomes.

