"""
Funcões - def me python (Parte 1)
"""
#EXEMPLO 1(so pra entender, n é usado realmete assim)
# def Saudacao(msg ='ola', nome='usuario'):#padrao definido
#     nome = nome.replace('a', '4')
#     msg = msg.replace('a', '4')
#     print(msg, nome)

# Saudacao()# se vc não colocar nd ele vai pegar o padrao q vc definiu la
# Saudacao('oi gatin', 'tata')
# Saudacao('ola', 'tata')
# Saudacao('iae', 'mano')

# print()
# Saudacao('tata', 'ola')#se vc reparar ele executa por ordem a não ser q...
# Saudacao(nome='tata', msg='ola')# vc defina, se vc definir ele vai ficar
#                                 #com a mesma ordem de origem da função


#EXEMPLO 2
#É COMUMENTE USADO ASSIM
# def Saudacao(msg ='ola', nome='usuario'):
#     nome = nome.replace('a', '4')
#     msg = msg.replace('a', '4')
#     return f'{msg} {nome}'

# variavel = Saudacao()
# print(variavel)



"""exemplos do chat"""

#funçao sem parametro. isso tbm funciona
# def diga_ola():
#     print('oi fdp')

# diga_ola()


#Se não sabe quantos argumentos vai receber, pode usar *args:
# def soma_tudo(*numeros):
#     total = 0
#     for n in numeros:
#         total += n
#     return total

# print(soma_tudo(2, 4, 6))


"""ATIVIDADE DO CHATZINHOO!!! UHUU"""
##Q1
# def diga_ola(nome):
#     print(f'Olá, {nome}')

# diga_ola('Lucas')

##Q2

# def soma(n1, n2):
#     return n1 + n2

# resultado = soma(5, 7)
# print(resultado)

##Q3
# def verificar_idade(idade):
#     idade = int(idade)

#     de_maior = (idade >= 18)

#     msg = 'Maior de idade' if de_maior else 'Menor de idade'

#     return msg

# verificando = verificar_idade(20)
# print(verificando)

##Q4
# def dobrar(lista):

#     nova_lista = []

#     for i in lista:
#         nova_lista.append(i*2)

#     return nova_lista

# numeros = [1, 4, 3]
# resultado = dobrar(numeros)
# print(resultado)

##Q5

# def conta_vogais(palavra):
#     vogais = 'aeiouáéíóúâêôãõàèìòù'
#     contando = 0
#     todas_minusculas = palavra.lower()

#     for letra in todas_minusculas:
#         if letra in vogais:
#             contando += 1
#     return contando

# resultado = conta_vogais("Programação")
# print(resultado)







"""
Funcões - def me python (Parte 2)
"""
#EXEMPLO 1
# def divisao(n1, n2):
#     if n2 == 0:
#         return
    
#     return n1 /n2

# divide = divisao(8,2)

# if divide:
#     print(divide)
# else:
#     print('conta invalida')

# print(divisao(45,5))


#EXEMPLO 2

# def dumb():
#     return [1,2,3,4,5]
# var = dumb()
# print(var[0], type(var))


"""
Funcões - def me python (Parte 3)
"""
# EXEMPLO 1
# def func(*args):
#     print(args)

# lista = [1,2,3,4,5]
# print(*lista, sep='-')# O SEP="" É O SE PA RA DOR



# EXEMPLO 2
# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))

# func(1,2,3,4,5)#Tupla


# EXEMPLO 3
# def func(*args):
#     args = list(args)#agora é uma lista
#     args[0] = 20
#     print(args)

# func(1,2,3,4,5)


# EXEMPLO 4
# def func(*args):
#     print(args)

# lista = [1,2,3,4,5]
# lista2 = [10,20]

# func(lista)#lista empacotada
# func(*lista)#lista desempacotada 
# func(*lista, 35, 51, *lista2)#e aida posso add mais


# EXEMPLO 5
# def func(*args, **kwargs): #são argumentos com palavras chave
#     print(args)
#     print(kwargs)
#     print(kwargs['nome'], kwargs['sobrenome'])##se quiser acessa nome e
                                                ## sobrenome
# lista = [1,2,3,4,5]
# lista2 = [10,20] 
# func(*lista, *lista2, nome ='evi', sobrenome='wal')


# EXEMPLO 6
# def func(*args, **kwargs): #são argumentos com palavras chave
#     print(args)

#     idade = kwargs.get('idade')#esta verificando se em kwargs tem o
#                                     #   .  argumento 'idade '
#     if idade is not None:           #   .
#         print(idade)                #   .   pelo visto
#     else:                           #   .   só tem nome e sobrenome
#         print('Não existe idade')   #   .
#                                     #   .
#                                     #   .
# lista = [1,2,3,4,5]  #  ....................           
# lista2 = [10,20]     # \/                  \/
# func(*lista, *lista2, nome ='evi', sobrenome='wal')












"""
atividade chatzinho
"""
#Q1
"""
n = 7
range(2, 7) = [2, 3, 4, 5, 6]

7 % 2 → não dá 0

7 % 3 → não dá 0

7 % 4 → não dá 0

7 % 5 → não dá 0

7 % 6 → não dá 0
→ Nenhum divisor encontrado → ✅ É primo!

🔁 Exemplo com n = 9
range(2, 9) = [2, 3, 4, 5, 6, 7, 8]

9 % 3 == 0 → tem divisor além de 1 e 9
→ ❌ Não é primo


"""
# def eh_primo(n):
#     if n < 2:  # 0 e 1 NÃO são primos
#         return False

#     for i in range(2, n):  # testa se existe algum divisor entre 2 e n
#         if n % i == 0:  # se for divisível por algum desses, não é primo
#             return False

#     return True  # se chegou aqui, é primo






#Q2

# def inverter(texto):
#     tamanho = len(texto)
#     invertida = texto[tamanho::-1]
#     return invertida

# a = inverter('Python')
# print(a)


#Q3

# def maior_numero(lista):
#     return max(lista)

# print(maior_numero([4, 10, 2, 9]))


#Q4
#ideia maluca
# def contar_palavras(str):
#     palavra = str.split(' ')
#     junta = ','.join(palavra)
#     contador = 0
#     for virgula in junta:
        
#         if virgula == ',':
#             contador += 1
#     return contador

# print(contar_palavras('Hoje o dia está bonito'))

"""Correto"""
# def contar_palavras(frase):
#     palavras = frase.split()# ou split(' ')
#     return len(palavras)

# print(contar_palavras('Hoje o dia está bonito'))




#Q5
# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     elif n % 3 == 0:
#         return "Fizz"
#     elif n % 5 == 0:
#         return "Buzz"
#     else:
#         return n

# print(fizzbuzz(3))   
# print(fizzbuzz(5)) 
# print(fizzbuzz(15)) 
# print(fizzbuzz(4))  





# OUTRO EXERCICIO 





# # Q1

# def soma_pares(lista):
#     soma = 0 
#     for numero in lista:
#         if numero %2 == 0:
#             soma = soma + numero
#     return soma

# print(soma_pares([1, 2, 3, 4, 5, 6]))





#Q2
# def fatorial(n):
#     resultado = 1 

#     for numero in range(1, n + 1):

#         resultado = resultado * numero

#     return resultado
# print(fatorial(5))




#Q3

# def eh_palindromo(palavra):
#     return palavra == palavra[::-1]

# print(eh_palindromo("ana"))      # True
# print(eh_palindromo("python"))   # False


# def eh_palindromo(palavra):
#     tamanho = len(palavra)

#     invertida = palavra[tamanho::-1]

#     if invertida == palavra:
#         return True
#     else:
#         return False
# print(eh_palindromo("ana"))    
# print(eh_palindromo("python"))  




#Q4

# def media(lista):

#     tamanho = len(lista)
#     soma = 0
#     for numero in lista:
#         soma += numero
#         media = soma / tamanho
#     return media
# print(media([5, 10, 15]))



# #Q5


# def contar_letras(palavra, letra):
#     palavra = palavra.lower()
#     letra = letra.lower()
#     return palavra.count(letra)

# print(contar_letras("Abacate", "a"))


"""
Funcões - def me python (Parte 4)
"""
#EXEMPLO 1
# variavel = 'valor'          # ESSA VARIAVEL O ESCOPO É GLOBAL
#                             # OBSERVA-SE A AÇÃO DO ESCOPO                             #  .
# def func():                 #
#     print(variavel)         #
#                             #
#                             #
# def func2():                # CADA FUNCAO TEM U ESCOPO LOCAL
#     variavel = 'Outro valor'#
#     print(variavel)         #
#                             #
# func()                      #
# func2()                     #
# print(variavel)             #


#EXEMPLO 2
variavel = 'valor'         
                                                        
def func():                 
    print(variavel)         
                            
                            
def func2(arg = None):               
    arg = arg.replace('v', 'c')
    return arg         
                            
func()                      
outra = func2(arg=variavel)
print(outra)          

