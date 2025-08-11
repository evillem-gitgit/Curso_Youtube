# QUESTAO 1 Listas

'''#COM FOR
# para cada item(i) na contagem de 1 á 11:   for i in range(1, 11)
#adicione os i na lista:    lista.append(i)'''

# lista = []

# for item in range(1, 11):
#     lista.append(item)
# print(lista)



# '''#COM While
# # Enquanto item(i) menor igual a 10:   while i <= 10:
# #adicione os i na lista:    lista.append(i)
# # i += 1: incrementa i em 1 a cada iteração.'''

# lista = []
# i = 1

# while i <= 10:
#     lista.append(i)
#     i = i + 1

# print(lista)



# # A)
# '''FOR'''
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in lista:
#     if i % 2 == 0:
#         print(i) 

# '''WHILE'''
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0

# while i < len(lista):
#     if lista[i] % 2 == 0:
#         print(lista[i])
#     i = i + 1


# # B)
# lista.append(11)
# print(lista)

# # C)
# lista.remove(5)
# print(lista)




#QUESTAO 2 Listas

# nomes = ["Bruno", "Carlos", "Diana", "Ana"]
# # A)
# nomes[2] = "Caio"
# print(nomes)

# # B)
# nomes.sort()
# print(nomes)
# print(sorted(nomes))
# nomes.sort(reverse=True)
# print(nomes)

# C)
# nomes = ["Bruno", "Carlos", "Diana", "Ana"]
# print(nomes[-1])



#Quest 3'''Tuplas'''
# A)

import locale
locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil') 

import calendar

meses = tuple(calendar.month_name[1:])  # Do mês 1 ao 12
# print(meses, "\n")
# print(calendar.month_name[4])

# # B)
# if 'junho' in meses:
#     print(meses.index('junho'))

# print(meses[5])ww


#C)
#print(len(meses))


# 4 Tuplas
numeros = (10, 20, 30, 40, 50)
#A)
# soma = 0
# for n in numeros:
#     soma = soma + n
# print(soma)

#B)
# AgoraÉlista = list(numeros)
# AgoraÉlista.append(60)
# print(AgoraÉlista)



# 5 Dicionarios
aluno = {

    "nome": "jao",
    "idade": 15,
    "notas":[10, 8, 5]
    
}

# #A)
# print(aluno["nome"])

#B)
# soma = 0
# for n in aluno["notas"]:
#     soma = soma + n

# media = soma / len(aluno["notas"])
# print(media)

#C) c) Adicione uma nova chave chamada aprovado
# com valor True ou False baseado na média (>= 7 é aprovado).

# aluno["Aprovado"] = media >= 7
# print(aluno["Aprovado"])


# 6 Dicionarios
# estoque = {"banana": 15,
#             "maçã": 8,
#             "laranja": 12}

# #A)Atualize o estoque de "maçã" para 10.

# estoque["maçã"] = 10
# print(estoque)

# #B)b) Remova "laranja" do dicionário.
# estoque.pop("laranja")
# print(estoque)

# #C) Adicione um novo item: "uva" com valor 20.
# estoque["uva"] = 20
# print(estoque)


# #7
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

#A) União dos conjuntos A e B.
#print(A | B)

#B) Interseção(tem em comum) entre A e B.
#print(A & B)

#C) Diferença de A para B.
#print( A - B)

#8
nomes = {"Ana", "Bruno", "Carlos", "Ana", "Carlos"}

#A) Quantos nomes únicos existem?
QtdDeNomes = len(nomes)
print(QtdDeNomes)

#B) Adicione o nome "Diana" ao conjunto.
nomes.add("Diana")
print(nomes)

#C)Remova "Bruno".
nomes.remove("Bruno")
print(nomes)