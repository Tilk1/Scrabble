#"windows" if "win" in sys.platform else "linux"
from pattern.es import *
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
        else:
            return "no_existe"


#palabra = input("Ingrese la palabra a evaluar : ")
#print(tipoPalabra(palabra))