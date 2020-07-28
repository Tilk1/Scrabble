import random


a = {(0, 0): 'vacio.png', (0, 1): 'lx2.png', (0, 2): 'vacio.png', (0, 3): 'vacio.png', (0, 4): 'px3.png', (0, 5): 'lx3.png', (0, 6): 'vacio.png', (0, 7): 'lx2.png', (0, 8): 'vacio.png', (0, 9): 'lx3.png', (0, 10): 'px3.png', (0, 11): 'vacio.png', (0, 12): 'vacio.png', (0, 13): 'lx2.png', (0, 14): 'vacio.png', (1, 0): '-1.png', (1, 1): 'px2.png', (1, 2): 'vacio.png', (1, 3): 'vacio.png', (1, 4): 'vacio.png', (1, 5): 'vacio.png', (1, 6): 'vacio.png', (1, 7): 'vacio.png', (1, 8): 'vacio.png', (1, 9): 'vacio.png', (1, 10): 'vacio.png', (1, 11): 'vacio.png', 
(1, 12): 'vacio.png', (1, 13): 'px2.png', (1, 14): '-1.png', (2, 0): 'vacio.png', (2, 1): 'vacio.png', (2, 2): 'vacio.png', (2, 3): '-3.png', (2, 4): 'vacio.png', (2, 5): 'vacio.png', (2, 6): 'vacio.png', (2, 7): 'vacio.png', (2, 8): 'vacio.png', (2, 9): 'vacio.png', (2, 10): 'vacio.png', (2, 11): '-3.png', (2, 12): 'vacio.png', (2, 13): 'vacio.png', (2, 14): 'vacio.png', (3, 0): 'vacio.png', (3, 1): 'vacio.png', 
(3, 2): 'lx3.png', (3, 3): 'vacio.png', (3, 4): 'vacio.png', (3, 5): 'px2.png', (3, 6): 'lx2.png', (3, 7): 'vacio.png', (3, 8): 'lx2.png', 
(3, 9): 'px2.png', (3, 10): 'vacio.png', (3, 11): 'vacio.png', (3, 12): 'lx3.png', (3, 13): 'vacio.png', (3, 14): 'vacio.png', (4, 0): 'vacio.png', (4, 1): 'lx3.png', (4, 2): 'vacio.png', (4, 3): 'vacio.png', (4, 4): 'vacio.png', (4, 5): 'lx2.png', (4, 6): '-1.png', (4, 7): 'vacio.png', (4, 8): '-1.png', (4, 9): 'lx2.png', (4, 10): 'vacio.png', (4, 11): 'vacio.png', (4, 12): 'vacio.png', (4, 13): 'lx3.png', (4, 14): 'vacio.png', (5, 0): 'lx3.png', (5, 1): 'vacio.png', (5, 2): 'vacio.png', (5, 3): 'px2.png', (5, 4): 'lx2.png', (5, 5): 'vacio.png', (5, 6): 'lx3.png', (5, 7): 'vacio.png', (5, 8): 'lx3.png', (5, 9): 'vacio.png', (5, 10): 'lx2.png', (5, 11): 'px2.png', (5, 12): 'vacio.png', 
(5, 13): 'vacio.png', (5, 14): 'lx3.png', (6, 0): 'vacio.png', (6, 1): 'vacio.png', (6, 2): 'vacio.png', (6, 3): 'lx2.png', (6, 4): 'vacio.png', (6, 5): 'vacio.png', (6, 6): 'vacio.png', (6, 7): 'vacio.png', (6, 8): 'vacio.png', (6, 9): 'vacio.png', (6, 10): 'vacio.png', (6, 11): 'lx2.png', (6, 12): 'vacio.png', (6, 13): 'vacio.png', (6, 14): 'vacio.png', (7, 0): 'px3.png', (7, 1): '-2.png', (7, 2): 'vacio.png', (7, 3): 'vacio.png', (7, 4): '-1.png', (7, 5): 'vacio.png', (7, 6): 'vacio.png', (7, 7): 'play.png', (7, 8): 'vacio.png', (7, 9): 'vacio.png', (7, 10): '-1.png', (7, 11): 'vacio.png', (7, 12): 'vacio.png', (7, 13): '-2.png', (7, 14): 'px3.png', (8, 0): 'vacio.png', (8, 1): 'vacio.png', (8, 2): 'vacio.png', (8, 3): 'lx2.png', (8, 4): 'vacio.png', (8, 5): 'vacio.png', (8, 6): 'vacio.png', (8, 7): 'vacio.png', (8, 8): 'vacio.png', (8, 9): 'vacio.png', (8, 10): 'vacio.png', (8, 11): 'lx2.png', (8, 12): 'vacio.png', (8, 13): 'vacio.png', (8, 14): 'vacio.png', (9, 0): 'lx3.png', (9, 1): 'vacio.png', (9, 2): 'vacio.png', (9, 3): 'px2.png', (9, 4): 'lx2.png', (9, 5): 'vacio.png', (9, 6): 'lx3.png', (9, 7): 'vacio.png', (9, 8): 'lx3.png', (9, 9): 'vacio.png', (9, 10): 'lx2.png', (9, 11): 'px2.png', (9, 12): 'vacio.png', (9, 13): 'vacio.png', (9, 14): 'lx3.png', (10, 0): 'vacio.png', (10, 1): 'lx3.png', (10, 2): 'vacio.png', (10, 3): 'vacio.png', (10, 4): 'vacio.png', (10, 5): 'lx2.png', (10, 6): '-2.png', (10, 7): 'vacio.png', (10, 8): '-2.png', (10, 9): 'lx2.png', (10, 10): 'vacio.png', (10, 11): 'vacio.png', (10, 12): 'vacio.png', (10, 13): 'lx3.png', (10, 14): 'vacio.png', (11, 0): 'vacio.png', (11, 1): 'vacio.png', (11, 2): 'lx3.png', (11, 3): 'vacio.png', (11, 4): 'vacio.png', (11, 5): 'px2.png', (11, 6): 'lx2.png', (11, 7): 'vacio.png', (11, 8): 'lx2.png', (11, 9): 'px2.png', (11, 10): 'vacio.png', (11, 11): 'vacio.png', (11, 12): 'lx3.png', (11, 13): 'vacio.png', (11, 14): 'vacio.png', (12, 0): 'vacio.png', (12, 1): 'vacio.png', (12, 2): 'vacio.png', (12, 3): '-3.png', (12, 4): 'vacio.png', (12, 5): 'vacio.png', (12, 6): 'vacio.png', (12, 7): 
'vacio.png', (12, 8): 'vacio.png', (12, 9): 'vacio.png', (12, 10): 'vacio.png', (12, 11): '-3.png', (12, 12): 'vacio.png', (12, 13): 'vacio.png', (12, 14): 'vacio.png', (13, 0): '-1.png', (13, 1): 'px2.png', (13, 2): 'vacio.png', (13, 3): 'vacio.png', (13, 4): 'vacio.png', (13, 5): 'vacio.png', (13, 6): 'vacio.png', (13, 7): 'vacio.png', (13, 8): 'vacio.png', (13, 9): 'vacio.png', (13, 10): 'vacio.png', (13, 11): 
'vacio.png', (13, 12): 'vacio.png', (13, 13): 'px2.png', (13, 14): '-1.png', (14, 0): 'vacio.png', (14, 1): 'lx2.png', (14, 2): 'vacio.png', (14, 3): 'vacio.png', (14, 4): 'px3.png', (14, 5): 'lx3.png', (14, 6): 'vacio.png', (14, 7): 'lx2.png', (14, 8): 'vacio.png', (14, 9): 'lx3.png', (14, 10): 'px3.png', (14, 11): 'vacio.png', (14, 12): 'vacio.png', (14, 13): 'lx2.png', (14, 14): 'vacio.png'}


b = {(7, 7): 'L.png', (4, 11): 'RR.png', (2, 5): 'L.png', (1, 8): 'O.png', (3, 9): 'M.png'}


elegida = (random.choice(list(a)))

print(elegida)

if elegida in b.keys():
    print('in here bro')
else:
    print('no esta')

  

# if (7,7) in b.keys():
#     print(type(c))
#     print('existe bro')