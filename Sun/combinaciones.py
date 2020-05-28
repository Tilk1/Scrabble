from itertools import permutations
from pattern.es import *
from pattern.web import Wiktionary
import funciones
import pattern.text.es
import itertools

ingreso = input('ingrese poqitas letras pq sino se traba (pone paz please): ')
print('estas son las palabras que se forman con esas letras:')


letras=str(input('ingrese letras')).split(' ')
print(letras)
combinaciones=list(itertools.permutations(letras))
for x in combinaciones:
    palabra=''
    for y in x:
        palabra=palabra+y
    print(palabra)


for p in permutations(ingreso):  ##pruebo todas las combinaciones posibles
    combinacion = (''.join(p))
    if(funciones.tipoPalabra(combinacion)!="no_existe"):
        print(combinacion, "es un: ", funciones.tipoPalabra(combinacion))  ##imprimo solo las palabras q existen