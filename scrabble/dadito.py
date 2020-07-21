from multiprocessing import Process, Lock, Value
from ctypes import c_bool
import time

def robot1(n, lock):
    while True:
        with lock:
            n.value = False
            print(n.value)
        time.sleep(1)

def robot2(n, lock):
    while True:
        with lock:
            n.value = True
            print(n.value)
        time.sleep(1)


if __name__ == '__main__':
    n = Value(c_bool, False)
    lock = Lock()
    Process(target=robot1, args=(n, lock)).start() 
    Process(target=robot2, args=(n, lock)).start()