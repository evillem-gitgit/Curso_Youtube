"""
Formatando valores com modificadores - Aula 5

:s - texto (string)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(número)f - quantidade de casas decimais (float)
:(caracter) (> ou < ou ^) (quantidade)(tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

# num1 = 10
# num2 = 3
# divisao = num1 / num2
# print('{:.2f}'.format(divisao) ) #:.(número)f
# print(f'{divisao:.2f}')          #:.(número)f

# nome = 'Luiz Otávio'
# print(f'{nome:s}')      # só diz que nome é uma string 
#                         # o mesmo que nome = str('Luiz Otávio')

# print(len(nome))
# print(f'{nome:#^24}')   #:(caracter) (> ou < ou ^) (quantidade)


# #o que esta dentro das chaves é o valor q esta no parentese dps de format
# nomeFormatado = '{n:0<30}'.format(n=nome) #format normal
# print(nomeFormatado)

# sobrenome = 'Pinto' 
#              #indice        #indice          #0       #1
# nomeFormatado = '{0:0<20}  {1:#<20}'.format(nome, sobrenome)
# print(nomeFormatado) 

# nomeNew = 'jao Felca'
# # nomeNew = nomeNew.ljust(20, '^')
# # print(nomeNew)

# print(nomeNew.lower()) #tudo minusculo
# print(nomeNew.upper()) #tudo maiusculo
# print(nomeNew.title()) #primeiras letras maiusculas

""" OUTRAS COISAS- MNIPULAÇAO DE STRINGS"""

# #positivo   [0122345678]
# texto     = 'Python s2'
# #negativo   -[987654321]


#                #começa    #termina
# novaStr = texto[  2  :      6  ] #ele printa do indice 2 ao 6
# print(novaStr) 

# novaStr = texto[  -9  :  -3  ] #ele printa do indice 2 ao 6
# print(novaStr)



# novaStr = texto[-1]
# print(novaStr)

# novaStr = texto[-9]
# print(novaStr)

# # eu quero q va de 0 até o caracter 6 e que ele pule de 2 em 2
# novaStr = texto[0:6:2]
# print(novaStr)



"""-------------------------------------------------------------------"""
#While com break e continue

# contador = 0
# while contador < 10:

#     if contador == 3:
#         contador = contador + 1  ##contador += 1
#         break

#     print(contador)
#     contador +=1
# print('acabou')


# contador = 0
# while contador < 10:

#     if contador == 3:
#         contador = contador + 1
#         continue

#     print(contador)
#     contador = contador + 1
# print('acabou')


# x = 0 #coluna

# while x < 10:
#     y = 0 #linha

#     while y < 5:
#         print(f'{x},{y}')
#         y = y + 1
        
#     x = x + 1

# print('acabou')


# while True:
#     print()
#     num1 = input('Digite um número: ')
#     num2 = input('Digite outro número: ')
#     operador = input('Digite um operador: ')
#     sair = input('deseja sair? [s]im ou [n]ão: ')

#     if sair == 's':
#         break
# # se o numero não estier so numero
#     if not num1.isnumeric() or not num2.isnumeric():
#         print('Voce precisa digitar so numeros')
#         continue

#     num1 = int(num1)
#     num2 = int(num2)

#     if operador == '+':
#         print(num1 + num2)

#     elif operador == '-':
#         print(num1 - num2)
    
#     elif operador == '/':
#         print(num1 / num2)

#     elif operador == '*':
#         print(num1 * num2)

#     else:
#         print('operador invalido')


"""--------- aula - 8 curso youtube Otavio Miranda"""
# contador = 1
# acumulador = 1

# while contador <= 10:
#     print(contador, acumulador)
#     contador+=1
#     acumulador = acumulador + contador

# else:
#     print('cheguei no else')

"""------------------------------------------------------"""
# minhaString = 'o rato roueu a roupa do rei de roma'
# contador = 0 
# tamanhoString = len(minhaString)

# novaString = ''

# while contador < tamanhoString:
    
#     if minhaString[contador] == 'r'or minhaString[contador] == 'a':
#         novaString = novaString + minhaString[contador].upper()

#     else:
#         novaString = novaString + minhaString[contador]
#     contador += 1

#--------

# minhaString = 'o rato roueu a roupa do rei de roma'
# tamanhoString = len(minhaString)
# contador = 0 
# novaString = ''

# while contador < tamanhoString:
    
#     if minhaString[contador] == 'r':
#         novaString = novaString + minhaString[contador].upper()

#     else:
#         novaString = novaString + minhaString[contador]
#     contador += 1

# print(novaString)
    

#qual letra aparece mais na variavel 'minhaString'?


# while True:
#     minhaString = input('digite: ')
#     tamanhoString = len(minhaString)

#     contador = 0
#     contagem = 0 #guarda a maior quantidade de repetições encontrada até agora
#     letra = ''

#     while contador < tamanhoString:
        
#         conta = minhaString.count(minhaString[contador]) 
        
#         if contagem < conta and minhaString[contador].strip():# tira os espaços
#                                                         #entre e no final e começo
#             letra = minhaString[contador]
#             contagem = conta


#         contador += 1

#     print(letra, contagem)



# for n in lista:
#     cal = len(lista)
# print(cal)

# for n in lista:
#     print(f' "{n}",')

#-------------------------------------------------
#Aula 10
"""For in
Iterando strings com for
Função range(start=0, stop, step=1)"""
#ja vem padrao start=0 e step=1

#start = onde quer que inicie
#stop = onde termina
#step = pule de quanto em quanto

# for n in range(20, 10, -1):
#     print(n)


# texto = 'python'
# novoTexto = ''
              
# for lentra in texto:

#     if lentra == 'p':
#       novoTexto = novoTexto + lentra.upper()

#     elif lentra == 'y':
#        novoTexto += lentra.upper()

#     else:
#        novoTexto += lentra    
# print(novoTexto)
      


# texto = 'Python'
#                 #ele vai enumerar os indices de cada letra
# for n, lentra in enumerate(texto):
#     print(n, lentra)


"""
Aula 11
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range"""

# #         0    1    2    3    4    5  
# lista = ['a', 'b', 'c', 'd', 'e', 10.5]
# print(lista[0:5:2])

# # ou
# #         0    1    2    3    4    5  
# lista = ['a', 'b', 'c', 'd', 'e', 10.5]
# tam = len(lista)
# print(lista[0:tam:2])

#         0    1    2    3    4    5  
# lista = ['a', 'b', 'c', 'd', 'e', 10.5]
# print(lista[0:5:2])
# print(lista[:5:2])
# print(lista[::-1])

# l1 =[1,2,3]
# l2=[4,5,6]
# print(f'l1 novinha: {l1}')
# print(f'l2 novinha: {l2}')


# l1.extend('a')
# print(f'l1 extend: {l1}') # a l1 roubou a l2

# l2.append('b')
# print(f'l2 com append: {l2}')

# l2.insert(0, 'banana')#escolhe o indice
# print(f'l2 com insert: {l2}')

# l2.pop()# remove o ultimo
# print(f'l2 com pop: {l2}')


"""
# lista1 = list(range(1,11))  
# print(lista1,'\n')
"""
# lista2 = [i for i in range(1, 11)]
# print(lista2, '\n')

# lista3 = []

# for i in range(1, 11):
#     lista3.append(i)

# print(lista3)


# lista = list(range(1,11)) 
# del(lista[3:5])#começa no 3 termina no 5 indice!
# print(lista)
 
# secreto = 'perfume'
# digitadas = []
# chances = 3

# while True:
#     if chances <=0:
#         print('voce perdeu!!')
#         break

#     letra = input('digite uma letra: ')

#     if len(letra) > 1:
#         print('ahh isso não vale, digite só uma por vez.')
#         continue #se eu adicionar mais de uma letra ele vai continuar
#                 # executando la do começo, se for so uma, ele vai add
#                 #||
#                 #\/

#     digitadas.append(letra)

#     if letra in secreto:
#         print(f'uhuuu,a letra "{letra}" existe na palavra secreta.')

#     else:
#         print(f'afff, a letra "{letra}" não exite na palavra secreta.')
#         digitadas.pop()

#     secreto_temporario = ''

#     for letra_secreta in secreto:

#         if letra_secreta in digitadas:
#             secreto_temporario += letra_secreta
#         else:
#             secreto_temporario += '*'
#               #.........................................
#                                                      # .
#     if secreto_temporario == secreto:                # .
#         print("Que legal, vc ganhou!!!!!!")          # .
#         break                                        #\/
#     else:
#         print(f'a palavra secreta esta assim: {secreto_temporario}')

#     if letra not in secreto:
#         chances -= 1
    
#     print(f'voce ainda tem {chances} chances.')
#     print()


