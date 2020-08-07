# ScrabblleAR
![](https://i.imgur.com/O7vRM8o.png)


## Requisitos

Python 3.6

PySimpleGUI (Libreria)

Pattern (Libreria)

Microsoft Visual C++ 14.0 + (Para el pattern y solo en windows)

## Instrucciones Linux
Usuarios de Linux: El programa es compatible. Solo se debe hacer un pip install de cada libreria y tener python 3.6
Sin embargo si se desea utilizar el entorno virtual ofrecido en catedras (https://archivos.linti.unlp.edu.ar/index.php/s/t9enmc3IlRfkDtz)  deberan hacer algunas modificaciones.
Al parecer la carpeta de PySimpleGUI tiene problemas como ya viene instalada. Asique se debe volver a descargar o reemplazar por
una que funcione. Aqui estan los pasos que me han funcionado:
1. En primer lugar utilizar la version 3.6.3 de python como interprete
2. Ir a la libreria PySimpleGUI y borrar la carpeta. La misma se encuentra en: /usr/local/lib/python3.6/dist-packages   Reemplazarla por la que se puede decargar de aqui: https://github.com/Tilk1/seminario_python
(Es posible que tambien funcione borrando la carpeta y volviendo a hacer un pip install PySimpleGUI)
3. A jugar!

## Instrucciones Windows para jugar rapido:

1. Descargar e instalar python https://www.python.org/ftp/python/3.6.3/python-3.6.3-embed-amd64.zip
2. Abrir una consola y ejecutar comando pip install pattern
3. Desde la misma consola cuando haya terminado ejecutar comando  pip install PySimpleGUI
4. Descargar la version Jugar 1.1 https://github.com/Tilk1/ScrabblleUNLPAgusSanti/archive/1.1.zip  , abrir carpeta scrabble, ejecutar JUGAR.pyw

## Instrucciones opcionales para desarrolladores

Hay dos opciones de correr el juego: 
1. La primera por medio de un IDE, seleccionando abrir carpeta ScrabblleUNLPAgusSanti y luego ejecutando ScrabbleAR.py
2. La segunda opcion es desde la branch version_JUGAR. O la ultima release Version jugar 1.1. Esta version incluye directamente un pyw que se ejecuta sin necesidad
de ningun IDE y tampoco muestra ninguna consola. Los requisitos siguen siendo los mismos. Se debe tener por defecto la version
3.6 de python(con el comando "py -0" podemos saber nuestra version por defecto), la libreria de pattern y la libreria de pySimpleGUI

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

