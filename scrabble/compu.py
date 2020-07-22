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
    print(combinaciones.intenta_las_combinaciones_quitando_una_letra(string_letras_maquina))

    ## se para en una posicion al azar de libres
    elegida = (random.choice(list(tableroIm)))

    # comprueba que la casilla no este ocupada
    print(tableroFichas.keys())
    if elegida in tableroFichas.keys():
        print('la posicion:', elegida, 'esta ocupada')
    else:
        print('esta disponible')

    return


    