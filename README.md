# ScrabblleAR
![](https://i.imgur.com/O7vRM8o.png)


## Requisitos

Python 3.6  (NO FUNCIONA VERSIONES POSTERIORES 3.8 NI 3.7)  Link: (https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe)

PySimpleGUI (Libreria) 4.16.0

Pattern (Libreria)

## Instrucciones Linux
Usuarios de Linux: El programa es compatible. Solo se debe hacer un pip install de cada libreria y tener python 3.6
Sin embargo si se desea utilizar el entorno virtual ofrecido en catedras (https://archivos.linti.unlp.edu.ar/index.php/s/t9enmc3IlRfkDtz)  deberan hacer algunas modificaciones.
Al parecer la carpeta de PySimpleGUI tiene problemas como ya viene instalada. Asique se debe volver a descargar o reemplazar por
una que funcione. Aqui estan los pasos que me han funcionado:
1. En primer lugar utilizar la version 3.6.3 de python como interprete
2. Ir a /usr/local/lib/python3.6/dist-packages y borrar la carpeta PySimpleGUI. Reemplazarla por la que se puede decargar de aqui: https://github.com/Tilk1/seminario_python
(Es posible que tambien funcione borrando la carpeta y volviendo a hacer un pip install PySimpleGUI)
3. Correr dentro de la carpeta scrabble  el archivo  ScrabbleAR.py
4. A jugar!

## Instrucciones Windows
1. Instalar esta version de python 3.6 (Link: (https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe))
2. Instalar PySimpleGUI (Libreria) 4.16.0  por medio de la consola de comandos,  pip install pysimplegui. Para ello se recomienda setear las variables de entorno de python
3. Instalar pattern por medio de pip install pattern
4. Correr dentro de la carpeta scrabble  el archivo  ScrabbleAR.py

## Windows .exe (sin instalar nada)
1. Descargar https://github.com/Tilk1/ScrabblleUNLPAgusSanti/archive/0.9.zip
2. Correr ScrabbleAR.exe

Nota: Esta version esta en fase de desarrollo y tiene menos funcionalidades. Tambien presenta bugs y no cuenta con pattern aun

## Jugando. Algunas reglas

Para comenzar la partida se debe ingresar un nombre luego tocar la opcion Jugar, y finalmente 'iniciar'. Es opcional entrar
a configuraciones.
La primera palabra debe pasar por el centro del tablero.
Las casillas especiales tienen bonus positivos o negativos de puntos
Al colocar las fichas en el tablero estas se pueden quitar individualmente tocando sobre la ultima colocada, en caso de querer sacar todas se usa el botón 'sacar todas' como antes dicho. En el caso de tener una ficha en mano y arrepentirse de colocarla en el tablero, si se presiona la posición de la ficha en donde estaba en el átril, esta vuelve a donde estaba. 



## Capturas de pantalla del juego

![](https://i.imgur.com/qOjQ1NO.png)
![](https://i.imgur.com/45gNJkF.png)
![](https://i.imgur.com/VVULFtw.png)




###### (Nota: Las imagenes podrian tener diferencias con la version final)

## Participantes

Maria Agustina Gonzalez y Santiago Jose Lizondo Colomes.

