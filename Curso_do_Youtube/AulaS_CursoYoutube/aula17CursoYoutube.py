"""
Aula 17 - lambda
"""
# EXEMPLO 1

# def funcao(argumento, argumento2):

#     return argumento *argumento2

# print(funcao(2,2))

# A MESMA COISA AQUI ABAIXO

# a = lambda x, y: x * y
# print(a(2,2))


# EXEMPLO 2

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# def func(item):
#     return item[1]

# lista.sort(key=func)
# print(lista)

# lista.sort(key=func, reverse=True) # o sort() ordenando pelo reverso.
# print(lista)

"""
A função sort() serve para ordenar os elementos da lista,
e o argumento key=func diz ao Python COMO ele deve comparar os elementos.

Ou seja, ele não vai ordenar pelas sublistas inteiras,
mas sim pelo valor que a função func retorna para cada sublista.



Você também poderia escrever assim, sem criar uma função separada:
"""
# EXEMPLO 3

listaa = [
    ['P1', 3, 13],
    ['P2', 2, 6],
    ['P3', 5, 7],
    ['P4', 4, 50],
    ['P5', 1, 8],
]
listaa.sort(key=lambda item: item[1])
print(listaa)
#                            vou pelo item: do indice 1
nova_lista = sorted(listaa, key=lambda item: item[2])
print(nova_lista)                           

"""
sort()!!!!!!!!!!!!
É um método que só funciona em listas.

Modifica a lista original (faz a ordenação "no lugar").

Não retorna uma nova lista, retorna None.

lista = [3, 1, 2]
lista.sort()
print(lista)  # [1, 2, 3]


#########################################################################


sorted()!!!!!!!!!!!!
É uma função embutida (built-in), funciona com qualquer iterável
(listas, tuplas, dicionários, sets...).

Não modifica o original, retorna uma nova lista ordenada.

Pode ser usada até com tuplas (que são imutáveis).


lista = [3, 1, 2]
nova_lista = sorted(lista)
print(nova_lista)  # [1, 2, 3]
print(lista)       # [3, 1, 2] (continua igual)
"""