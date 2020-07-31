from pattern.text.es import verbs, tag, spelling, lexicon, parse
from sys import platform as _platform
import os

def clasificar(cual):
    if cual == "JJ":
        return "adjetivos"
    elif cual == "VB":
        return "verbos"
    else:
        return 'sustantivos'

def tipoPalabra(d):
    palabra = d
    analisis = parse(palabra, tags=True, chunks=False).split(' ')
    tipo = clasificar(analisis)
    #if len(palabra) == 1:      SIRVE PARA TESTEAR POR AHORA
    #    return 'no_existe'
    if(tipo == 'sustantivos'):
        if not palabra.lower() in verbs:
            if not palabra.lower() in spelling:
                if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
                    return 'no_existe'
                else:
                    return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])            
            else:
                return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
        else:
            return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
    else:
        return tipo

print(tipoPalabra('correr'))