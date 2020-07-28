import time
import random
import combinaciones
def turno_maquina(tableroIm, tableroFichas, letrasM, window, colores, bolsa):
    
    ###  hace tiempo para que corra el gif y quede bonito ###
    segundos_de_loop = time.time() + 2
    image = window['gifcompu']
    while time.time()  < segundos_de_loop:
        window.read(10)
        image.update_animation('imagenes/robot.gif', 150)
    image.update('imagenes/robot.gif')
    print('TENGO ESTAS FICHAS:')
    print(letrasM)

    ### une las letras del diccionario en un solo string para obtener la palabra ###
    string_letras_maquina = ''
    for i in letrasM.items():
        string_letras_maquina = string_letras_maquina +  i[1].split('.')[0]

    ## Obtiene la palabra que puede formar
    print('PUEDO FORMAR LA PALABRA:')
    formada = (combinaciones.intenta_las_combinaciones_quitando_una_letra(string_letras_maquina))
    tamaño = len(formada)
    print('la palabra formada es: ', formada, 'de tamaño: ', tamaño)

    if formada != ('no_encontro'):
        ## se para en una posicion al azar de libres
        pos_elegida = (random.choice(list(tableroIm)))
        coord_x = pos_elegida[0]
        print('cordenada X : ',coord_x)
        coord_y = pos_elegida[1]
        print('cordenada Y : ',coord_y)

        # comprueba que las casillas no esten ocupadas osea que no este en tableroFichas.Keys
        # Pero tambien debo verificar que existan esas posiciones en el tablero, para q no se vaya a la cuarta dimension
        print('OCUPADAS POR EL MOMENTO: ', tableroFichas.keys())

        todas_disponibles = True

        for i in range(tamaño):
            if ((coord_x , i + coord_y) not in tableroFichas.keys()) & ((coord_x , i + coord_y) in tableroIm):
                print('esta pos esta disponible: ', coord_x,i + coord_y)
            else:
                print('esta pos NO esta disponible: ', coord_x, i + coord_y)
                todas_disponibles = False
                break
        

        # si estan disponibles entonces las dibujo
        # tambien agrego al diccionario de ocupadas
        # y se las quito de sus letras disponibles dandole nuevas

        if todas_disponibles == True:
            for i in range(tamaño):
                coord = coord_x, i + coord_y
                window[(coord)].update(image_filename= (formada[i] + '.png'))
                tableroFichas.update({coord : formada[i] + '.png' })

        print(tableroFichas)

    else:     
        print('no he podido formar nada. Shame on me, paso turno')

    return
    