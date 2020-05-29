#"windows" if "win" in sys.platform else "linux"
from pattern.text.es import *
from pattern.web import Wiktionary

w = Wiktionary(language="es")

def tipoPalabra(arg):
    analisis = parse(arg).split('/')
    if analisis[1] == "JJ": 
        return "adjetivo"
    elif (analisis[1]) == "VB":
        return "verbo"
    elif (analisis[1] == "NN"):  # No distingue las no palabras de sustantivos, asiq usamos wiktionary en ese caso
        article=w.search(arg)
        if article!=None:
            return "sustantivo"
    return "no_existe"



def calcular_puntaje(palabra):
    i = 0
    suma = 0
    for char in palabra:
        letra = (palabra[i] + ".png")
        suma = suma + (bolsa[letra]['valor'])
        i = i+1
    print(suma)

    #test quitar esto revertir commit