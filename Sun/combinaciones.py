from itertools import permutations
from pattern.text.es import *
from pattern.web import Wiktionary
import funciones

ingreso = input('ingrese poqitas letras pq sino se traba (pone paz please): ')
print('estas son las palabras que se forman con esas letras:')


for p in permutations(ingreso):  ##pruebo todas las combinaciones posibles
    combinacion = (''.join(p))
    if(funciones.tipoPalabra(combinacion)!="no_existe"):
        print(combinacion, "es un: ", funciones.tipoPalabra(combinacion))  ##imprimo solo las palabras q existen