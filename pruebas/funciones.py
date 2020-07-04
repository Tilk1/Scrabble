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

puestas = {(7, 7): 'R.png', (7, 8): 'K.png', (7, 9): 'Z.png'} #solo para testear
bolsa={'A.png':{'cant':11,'valor':1}, 'B.png':{'cant':11,'valor':3}, 'C.png':{'cant':8,'valor':1},'D.png':{'cant':7,'valor':1}, 'E.png':{'cant':7,'valor':1}, 'F.png':{'cant':7,'valor':1}, 'G.png':{'cant':7,'valor':1}, 'H.png':{'cant':5,'valor':1}, 'I.png':{'cant':7,'valor':1}, 'J.png':{'cant':7,'valor':1}, 'K.png':{'cant':7,'valor':1}, 'L.png':{'cant':7,'valor':1},'M.png':{'cant':7,'valor':1},'N.png':{'cant':7,'valor':1},'Ñ.png':{'cant':7,'valor':1},'O.png':{'cant':7,'valor':1},'P.png':{'cant':7,'valor':1},'Q.png':{'cant':7,'valor':1},'R.png':{'cant':7,'valor':1},'S.png':{'cant':7,'valor':1},'T.png':{'cant':7,'valor':1},'U.png':{'cant':7,'valor':1},'V.png':{'cant':7,'valor':1},'W.png':{'cant':7,'valor':1},'X.png':{'cant':7,'valor':1},'Y.png':{'cant':7,'valor':1},'Z.png':{'cant':7,'valor':1},'LL.png':{'cant':7,'valor':1},'RR.png':{'cant':7,'valor':1}}
#la bolsa esta aca solo para testear. Hay q sacarla


def obtener_palabra(dict):
    palabraFormada = ''
    for x in dict:
	    palabraFormada = palabraFormada + (puestas[x].split('.')[0])
    return(palabraFormada)


calcular_puntaje(obtener_palabra(puestas))