from itertools import count

contador = count(start=10, step=-15)
lista = ['benjamin', 'juan', 'juan', 'jose', 'maria']
lista = zip(contador, lista)
print(list(lista))

