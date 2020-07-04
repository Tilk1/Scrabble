from itertools import permutations
from pattern.es import verbs, tag, spelling, lexicon
from pattern.web import Wiktionary
import funciones



##Las combinaciones funcionan usando todas las letras dadas.. Por ende si tenemos autos no va a encontrar nada
##tendriamos que pasarle las letras de a 1 para q vaya probando cada vez con mas letras las combinaciones y no todas juntas

def devuelve_primera_combinacion(palabra):
    for p in permutations(palabra):  ##pruebo todas las combinaciones posibles
      combinacion = (''.join(p))
      if (combinacion.lower() in verbs) or (combinacion.lower() in spelling) or (combinacion.lower() in lexicon) or (combinacion.upper() in lexicon) or (combinacion.capitalize() in lexicon):
        return(combinacion)  ##imprimo solo las palabras q existe
    return("no_hay")


palabra = input('ingrese algunas letras y se devuelve la primera combinacion posible: ')
print(devuelve_primera_combinacion(palabra))



##ESTO ARMA TODAS LAS PALABRAS POSIBLES Q EXISTEN, NO SERIA APLICABLE . ES AL PEDO

palabra = input('ingrese poqitas letras pq sino se traba: ')
print('estas son las palabras que se forman con esas letras:')
paso_prueba1= 0
paso_prueba2= 0

for p in permutations(palabra):  ##pruebo todas las combinaciones posibles
    combinacion = (''.join(p))
    print('COMBINACION A EVALUAR: ',combinacion)
    if (combinacion.lower() in verbs) or (combinacion.lower() in spelling) or (combinacion.lower() in lexicon) or (combinacion.upper() in lexicon) or (combinacion.capitalize() in lexicon):
        paso_prueba1 += 1  ##los OR  deberian tomar el primer caso , no hace todas las comprobaciones...
        if(funciones.tipoPalabra(combinacion)!="no_existe"):  ## ahora veo q tipo de palabra es
            paso_prueba2 += 1
            print(combinacion, "es un: ", funciones.tipoPalabra(combinacion))  ##imprimo solo las palabras q existe

print("pasaron prueba 1 : " ,paso_prueba1)
print("pasaron prueba 2 : " ,paso_prueba2)



