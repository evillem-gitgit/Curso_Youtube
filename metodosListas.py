

'''Tem a possibilidade de acessar o ultimo elemento
 sem saber quantos elementos temos na lista.
 È só colocar um valor negativo

lista = ["lets", 4, 8.2, False]

print(lista[-1], "Achando o ultimo da lista com N negativo(-1)")'''

####################################################

'''Metodo APPEND: Adiciona elementos no final da lista
lista = ["lets", 4, 8.2, False]
lista.append(True)
print(lista)
'''

#####################################################

'''o DEL remove uma função e o deu não é metodo, é uma função
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
del nomes[0]
print(nomes)
'''

#####################################################

'''Metodo REMOVE: tem que escrever qual elemento queremos remover,
não pela posição
lista = ["lets", 4, 8.2, False]

lista.append(True)
print(lista)
lista.remove(True)
print(lista)'''

#####################################################

'''lista[1] = "foca" : Isso é para alterar o valor
pela posição que vc quer substituir

lista = ["lets", "foda", "faca"]
print(lista)
lista[1] = "foca"
print(lista)
'''
#####################################################

'''Função LEN(): para saber a qtd de elementos de uma lista
lista = ["lets", 4, 8.2, False]
print(len(lista))
'''
#####################################################

'''As strings tambem se comportam como listas. Da para acessar os
caracteres de uma string pela posição como em uma lista

str_lets_data = "Let´s Data"
print(str_lets_data[6])
'''
#####################################################
"Uma vez criada a tupla, não pode mais ser mudada."
"Ou seja nada de adicionar, remover, ou mudar elementos."
'''

tupla = ("lets", 4, 8.2, False)
outra_tupla = 1, 2, 3, 'de oliveira'
print(outra_tupla)
print(outra_tupla[3])
'''
#####################################################
'''conjuntos--> o elemento repetido n é repetido quando executado.
            --> São desordenado

conjunto = {"lets", 4, 8.2, False}
conjunto_dois = {1, 1, 2, 2, "lets", "lets", "data"}
print(conjunto_dois)
'''

####################################################

'''metodo add(): é para conjuntos
                 serve para adicionar elemntos

conjunto = {"lets", 4, 8.2, False}
conjunto_dois = {1, 1, 2, 2, "lets", "lets", "data"}

conjunto_dois.add("oulha")
print(conjunto_dois)
'''
###################################################
'''metodo pop(): é para retornar um elementos e
 tbm remove ele ao mesmo tempo

conjunto = {"lets", 4, 8.2, False}
conjunto_dois = {1, 1, 2, 2, "lets", "lets", "data"}
conjunto_dois.pop(2)
'''


'''Operações entre conjuntos:
🟣 União (tudo, sem repetir):
python
Copiar código
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}


🔵 Interseção (elementos em comum):
python
Copiar código
print(a & b)  # {3}


🔴 Diferença (o que tem em a mas não em b):
python
Copiar código
print(a - b)  # {1, 2}


🟠 Diferença simétrica (o que só tem em um ou outro):
python
Copiar código
print(a ^ b)  # {1, 2, 4, 5}


🧠 Observações:
Conjuntos não têm índice, então não dá para acessar por posição.

Usado quando não importa a ordem e não pode haver repetições.'''
