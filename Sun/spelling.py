from pattern.es import lexicon, spelling, tag
import itertools
import funciones
def clasificar(palabra):
	print(tag(palabra, tokenize=True, encoding='utf-8', tagset = 'UNIVERSAL'))
	print(tag(palabra, tokenize=True, encoding='utf-8'))

letras=str(input('ingrese letras')).split(' ')
print(letras)
combinaciones=list(itertools.permutations(letras))
palabras=list()
for x in combinaciones:
    palabra=''
    for y in x:
        palabra=palabra+y
    palabras.append(palabra)
for x in palabras:
    if not x in spelling:
	    if x in lexicon:
		    print('La encontró en lexicon')
		    clasificar(x)
    else:
	    print('La encontró en spelling')
	    clasificar(x)