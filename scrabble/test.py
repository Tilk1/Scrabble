
letrasM = {'m0': 'L.png', 'm1': 'O.png', 'm2': 'T.png',
           'm3': 'R.png', 'm4': 'J.png', 'm5': 'V.png', 'm6': 'O.png'}

formada = 'LOV'

for i in formada:
    print(i)
    for key, value in letrasM.items():
        if (letrasM[key].split('.')[0]) == i:
            print('Eliminando letra: ', letrasM[key])
            letrasM[key] = ''
            break

print(letrasM)
