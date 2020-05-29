letrasU={'u0':'','u1':'','u2':'','u3':'A.png','u4':'','u5':'','u6':''}
letrasU=list(letrasU.items())
l=list(filter(lambda x:x[1]=='A.png',letrasU))[0][0]
print(l)
letrasU={'u0':'','u1':'','u2':'','u3':'A.png','u4':'','u5':'','u6':''}
letrasU.pop('u0')
print(letrasU)
