from itertools import permutations
#from pattern.es import verbs, tag, spelling, lexicon
#from pattern.web import Wiktionary
import funciones
from random import randrange
import pickle
import os
cwd = os.getcwd()


##Las combinaciones funcionan usando todas las letras dadas.. Por ende si tenemos autoz no va a encontrar nada
##tendriamos que pasarle las letras de a 1 para q vaya probando cada vez con mas letras las combinaciones y no todas juntas

def devuelve_primera_combinacion(palabra):
    """
    Devuelve un string con la primera combinacion formada valida (es decir q sea una palabra)
    o en caso de no encontrar devuelve el string "no_encontro".
    Las combinaciones funcionan usando todas las letras dadas.. Por ende si tenemos autoz no va a encontrar nada

    """
    file = open(os.path.join(cwd,'lista_palabras_arg.pickle'), 'rb')
    data = pickle.load(file)
    file.close()
    for p in permutations(palabra):  ##pruebo todas las combinaciones posibles
      combinacion = (''.join(p))
      if combinacion.lower() in data:
        return(combinacion)  # retorno la primera combinacion
    return("no_encontro")

vocales = ['A','E', 'I', 'O' , 'U']


def intenta_las_combinaciones_quitando_una_letra(palabra):
    """
    Esta funcion tiene dentro la funcion  devuelve_primera_combinacion. Como la anterior funcion exigia usar todas las letras
    existen veces que no se puede formar nada (como el ejemplo autoz)
    Por eso esta funcion va quitando letras del string. Por ejemplo si quitamos la z ya se puede formar autoz
    """
    formada = palabra
    while ((devuelve_primera_combinacion(formada) == "no_encontro") & (len(formada) >= 0 )): #mientras no formemos nada
        print('DEBUG ',formada)
        letra_azar = formada[randrange(len(formada))]
        if letra_azar in vocales:                ## si la letra al azar es una vocal
            letra_azar = formada[randrange(len(formada))]  # vuelvo a sacar otra
        nueva = ''
        encontramos = False
        for x in formada:
            if (x != letra_azar) or (encontramos == True):  #de esta forma nos aseguramos de borrar 1 sola
                nueva += x
            else:
                encontramos = True
        formada = nueva   #volvimos a armar la palabra sin la que quitamos

    if len(formada) == 1:
        return 'no_encontro'    
    else:
        return devuelve_primera_combinacion(formada)
        
