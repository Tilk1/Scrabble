from itertools import permutations
from pattern.es import verbs, tag, spelling, lexicon
from pattern.web import Wiktionary
import funciones


##Las combinaciones funcionan usando todas las letras dadas.. Por ende si tenemos autoz no va a encontrar nada
##tendriamos que pasarle las letras de a 1 para q vaya probando cada vez con mas letras las combinaciones y no todas juntas

def devuelve_primera_combinacion(palabra):
    """
    Devuelve un string con la primera combinacion formada valida (es decir q sea una palabra)
    o en caso de no encontrar devuelve el string "no_encontro".
    Las combinaciones funcionan usando todas las letras dadas.. Por ende si tenemos autoz no va a encontrar nada

    """
    for p in permutations(palabra):  ##pruebo todas las combinaciones posibles
      combinacion = (''.join(p))
      if (combinacion.lower() in verbs) or (combinacion.lower() in spelling) or (combinacion.lower() in lexicon) or (combinacion.upper() in lexicon) or (combinacion.capitalize() in lexicon):
        return(combinacion)  # retorno la primera combinacion
    return("no_encontro")

vocales = ['a','e', 'i', 'o' , 'u']


def intenta_las_combinaciones_quitando_una_letra(palabra):
    """
    Esta funcion tiene dentro la funcion  devuelve_primera_combinacion. Como la anterior funcion exigia usar todas las letras
    existen veces que no se puede formar nada (como el ejemplo autoz)
    Por eso esta funcion va quitando letras del string. Por ejemplo si quitamos la z ya se puede formar autoz
    """
    formada = palabra
    while ((devuelve_primera_combinacion(formada) == "no_encontro") & (len(formada) >= 0 )): #mientras no formemos nada
        print('DEBUG ',formada)
        if formada[len(formada)-1] == vocales[:]: ## si la ultima letra es una vocal
            formada = formada[+1:]                ## entonces sacamos la primera
        else:
            formada = formada[:-1]                ## sino sacamos la ultima
    if len(formada) == 1:
        return 'no_encontro'    
    else:
        return devuelve_primera_combinacion(formada)
        
