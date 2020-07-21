import multiprocessing
import time
import PySimpleGUI as sg
from random import randint

def Timer2():
    tuple = (20,20)
    sg.theme('Dark')
    sg.set_options(element_padding=(0, 0))
    form_rows = [[sg.Text(size=(8, 2), font=('Helvetica', 20),
                       justification='center', key='text')],
                 [sg.Button('Pause', key='-RUN-PAUSE-'),
                 sg.Button('Reset'),
                 sg.Exit(button_color=('white', 'firebrick4'))]]
    window2 = sg.Window('Running Timer', form_rows,
                        auto_size_buttons=False, location= tuple, grab_anywhere= True)
    i2 = 0
    paused2 = False
    start_time2 = int(round(time.time() * 100))

    while True:
        # This is the code that reads and updates your window
        button, values = window2.read(200)
        window2['text'].update('{:02d}:{:02d}.{:02d}'.format(
            (i2 // 100) // 60, (i // 100) % 60, i % 100))

        if values is None or button == 'Exit':
            break

        if button == 'Reset':
            i2 = 0
        

        elif button == '-RUN-PAUSE-':
            paused2 = not paused2
            window2['-RUN-PAUSE-'].update('Run' if paused2 else 'Pause')

        if not paused2:
            i2 += 1

    window2.close()


def Timer():
    sg.theme('Dark')
    sg.set_options(element_padding=(0, 0))
    form_rows = [[sg.Text(size=(8, 2), font=('Helvetica', 20),
                       justification='center', key='text')],
                 [sg.Button('Pause', key='-RUN-PAUSE-'),
                 sg.Button('Reset'),
                 sg.Exit(button_color=('white', 'firebrick4'))]]
    window = sg.Window('Running Timer', form_rows,
                       no_titlebar=False, auto_size_buttons=False)
    i = 0
    paused = False
    start_time = int(round(time.time() * 100))

    while True:
        # This is the code that reads and updates your window
        button, values = window.read(200)
        print(window.CurrentLocation())
        window['text'].update('{:02d}:{:02d}.{:02d}'.format(
            (i // 100) // 60, (i // 100) % 60, i % 100))

        if values is None or button == 'Exit':
            break

        if button == 'Reset':
            i = 0
        

        elif button == '-RUN-PAUSE-':
            paused = not paused
            window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')

        if not paused:
            i += 1

    window.close()


def robot1():
    Timer()

def robot2():
    Timer()

if __name__ == '__main__':
    r1 = multiprocessing.Process(name='r1', target=robot1)
    r2 = multiprocessing.Process(name='r2', target=robot2)
    r1.start()
    r2.start()










