"""
Aula 18 -
tuplas
"""
# for indice, valor in enumerate(tupla1):
#      print(indice, '-', valor)

# tupla1 = (1,2,3, 'a', 'mario')
# tupla2 = 4,5,6, 'b' # É tupla tbm
# t3  = tupla1 + tupla2

# item1, item2, *resto_lista , ultimo = t3
# print(resto_lista)

# posso ter uma tupla de um item só, contanto que tenha virgula(,)
# tpl = 1,
# print(tpl, type(tpl))

# EXEMPLO 2
tupla1 = (1,2,3,4,5)
tupla1 = list(tupla1)#transformei em lista
tupla1[1] = 3000 # mudei o valor
print(tupla1)
tupla1 = tuple(tupla1)# trasformei em tupla dnv
print(tupla1)