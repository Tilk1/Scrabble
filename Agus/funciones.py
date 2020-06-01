#"windows" if "win" in sys.platform else "linux"
from pattern.text.es import parse
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


def calcularPuntaje(l, im, b):
    suma=0
    multi=list()
    for x in l:
        cas=im[x]
        if (cas=='lx2.png'):
            suma=suma+(b[l[x]]['valor']*2)
        elif(cas=='lx3.png'):
            suma=suma+(b[l[x]]['valor']*3)
        elif(cas=='-1.png'):
            suma=suma+(b[l[x]]['valor']-1)
        elif(cas=='-2.png'):
            suma=suma+(b[l[x]]['valor']-2)
        elif(cas=='-3.png'):
            suma=suma+(b[l[x]]['valor']-3)
        elif(cas=='px2.png'):
            multi.append(2)
        elif(cas=='px3.png'):
            multi.append(3)
        else:
            suma=suma+b[l[x]]['valor']
    for y in multi:
        suma=suma*y
    return suma

#def calcular_puntaje(palabra):
#   i = 0
#    suma = 0
#    for char in palabra:
#        letra = (palabra[i] + ".png")
#        suma = suma + (bolsa[letra]['valor'])
#        i = i+1
#    return suma
#


def obtener_palabra(dict): ##esto funciona mandandole un diccionario dentro de la funcion colocar fichas, con un formato asi {(7, 7): 'R.png', (7, 8): 'K.png', (7, 9): 'Z.png'} 
    palabraFormada = ''
    for x in dict:
	    palabraFormada = palabraFormada + (dict[x].split('.')[0])
    return(palabraFormada)


def valor_del_tipo_de_palabra(tipo):  ## tendria q traer los valores de la config y no estar fijos aca
    if tipo == "adjetivo":
        return 15
    elif tipo == "verbo":
        return 10
    elif tipo == "sustantivo":
        return 5
    elif tipo == "no_existe": # este caso ni deberia existir
        return 0

#palabra = "PATO"
#print(tipoPalabra(palabra.lower()))