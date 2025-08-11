"""
Split - dividir uma string
Join - juntar uma lista str
strip() remove espaços no fim e começo
"""

string = "O brasil é o pais do futebol, o Brasil é penta."
lista1 = string.split(' ')# o split vai separa a str com base
                          #  no que você coloca

# print('lista 1')
# print("separou com base em espaços")
# print(lista1)
# print("\n")

lista2 = string.split(',')

# print('lista 2')
# print("separou com base em virgula")
# print(lista2)
#pelo visto ele separa trasformando em uma lista então...

#ex1
# for valor in lista1:
#     print(valor)# ele printou a cada laço um valor da lista

#ex2
# for valor in lista2:
#     print(valor.strip().capitalize())

# string2 = 'O Brasil é penta.'

# lista = string.split(' ')

# string3 = ','.join(lista) # o join() juntou com base na virgula
# print(string3)


###ENUMERATE
#ex1
# string2 = 'O Brasil é penta.'

# lista = string.split(' ')

# for indice, valor in enumerate(string):
#     print(indice, valor)


# L1
# lista = ['luiz','joao', 'maria']                               
                                                                      
# for indice, nome in enumerate(lista):                              
#     print(indice, nome)                                           

# # L1 E L2 FAZEM A MESMA COISA

#L2
# lista = [
#     [0,'luiz'],
#     [1,'joao'],
#     [2, 'maria'],
# ]

# for indice, nome in lista:
#     #     coluna coluna
#     print(indice, nome)  

                                                               
#-------------------------------------------------------- 
#TESTE OQ APRENDI FATIAMENTO
#Q1
# texto = "Programação em Python é divertida!"

# for indice, n in enumerate(texto):
#     print(indice, n)

# parte = texto[15:21:]
# print(parte, '\n')

#Q2
# parte = texto[33::-1]
# print(parte)

#Q3

# texto = "Programação em Python é divertida!"

# resultado1 = texto[::2]
# print(resultado1)
# #  OU

# nova_str = []

# for indice, n in enumerate(texto):
#     if indice %2 == 0:
#         nova_str.append(n)

# resultado2 = ''.join(nova_str)
# print(resultado2)
#--------------------------------------------------------
