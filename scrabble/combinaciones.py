from itertools import permutations
#from pattern.es import verbs, tag, spelling, lexicon
#from pattern.web import Wiktionary
from scrabble import funciones
from random import randrange
import pickle
import os
cwd = os.getcwd()


# Las combinaciones funcionan usando todas las letras dadas.. Por ende si tenemos autoz no va a encontrar nada
# tendriamos que pasarle las letras de a 1 para q vaya probando cada vez con mas letras las combinaciones y no todas juntas

def devuelve_primera_combinacion(palabra, data1, data2):
    """
    Devuelve un string con la primera combinacion formada valida (es decir q sea una palabra)
    o en caso de no encontrar devuelve el string "no_encontro".
    Las combinaciones funcionan usando todas las letras dadas.. Por ende si tenemos autoz no va a encontrar nada

    """
    limite = 0
    for p in permutations(palabra):  # pruebo todas las combinaciones posibles
        limite += 1
        combinacion = (''.join(p))
        if combinacion.lower() in data1 or combinacion.lower() in data2:
            return(combinacion)  # retorno la primera combinacion
        if limite == 30:
             return("no_encontro")
    return("no_encontro")


vocales = ['A', 'E', 'I', 'O', 'U']


def intenta_las_combinaciones_quitando_una_letra(palabra):
    """
    Esta funcion tiene dentro la funcion  devuelve_primera_combinacion. Como la anterior funcion exigia usar todas las letras
    existen veces que no se puede formar nada (como el ejemplo autoz)
    Por eso esta funcion va quitando letras del string. Por ejemplo si quitamos la z ya se puede formar autoz
    """
    formada = palabra
    file = open(os.path.join(cwd, 'lista_palabras_arg.pickle'), 'rb')
    data1 = pickle.load(file)
    file.close()
    file = open(os.path.join(cwd, 'lista_verbos_sin_acento.pickle'), 'rb')
    data2 = pickle.load(file)
    file.close()
    while ((devuelve_primera_combinacion(formada, data1, data2) == "no_encontro") & (len(formada) > 0)):  # mientras no formemos nada
        print('DEBUG ', formada)
        letra_azar = formada[randrange(len(formada))]
        if letra_azar in vocales:  # si la letra al azar es una vocal
            # vuelvo a sacar otra
            letra_azar = formada[randrange(len(formada))]
        nueva = ''
        encontramos = False
        for x in formada:
            # de esta forma nos aseguramos de borrar 1 sola
            if (x != letra_azar) or (encontramos == True):
                nueva += x
            else:
                encontramos = True
        formada = nueva  # volvimos a armar la palabra sin la que quitamos

    if len(formada) == 1:
        return 'no_encontro'
    else:
        return devuelve_primera_combinacion(formada,data1,data2)
