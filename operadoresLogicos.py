# """Operadores Logicos - aula 4
# and, or, not
# in e not in
# """
# pqp = []
# print(pqp)

# a = 2
# b = 2
# c = 3

# a == b and b < c
# """-----------------------------------------------------------------"""
# """not"""

# nomes = []

# if not nomes:
#     print("Lista está vazia")
# else:
#     print("Lista tem elementos")

# """Se a lista NÃO tem elementos."""




# """Negar o resultado de uma comparação
# Suponha que você queira executar algo se o usuário NÃO for admin:
# """

# usuario = "joao"

# if not usuario == "admin":
#     print("Acesso limitado")
# else:
#     print("Acesso total")

# """usuario == "admin" → False para “joao”.

# not False → True → imprime “Acesso limitado”.
# """


# """Combinar com expressões complexas
# Às vezes fica mais legível negar uma condição inteira
# em vez de inverter tudo dentro dela. Por exemplo:
# """
# idade = 20
# tem_autorizacao = True

# if not (idade >= 18 or tem_autorizacao):
#     print("Não pode entrar")
# else:
#     print("Pode entrar")

# """idade >= 18 or tem_autorizacao → True

# not True → False → imprime “Pode entrar”.
# """



# """-----------------------------------------------------------------"""


# """in"""

# nome = 'thalysson'

# if 't' in nome:   #"Se o 't' está em nome"
#     print("Existe")

# else:
#     print("não existe")


# """-----------------------------------------------------------------"""

# """not in"""

# nome = 'thalysson'

# if 't' not in nome:   #"Se o 't' Não está em nome"
#     print(" 't' nao Existe")

# else:
#     print("E xiste")


#Q1

# idade = str(input('digite idade:'))

# documento = str(input('diga se tem document:'))

# pessoa = {
#     'idade': idade,
#     'documento': documento
# }

# if '16' in pessoa['idade'] and 'sim' in pessoa['documento']:
#     print("Pode votar")

# else:
#     print("nao")


#Q2 DIFICULDADE

# n = int(input())

# if not n > 10 and not n < 20:
#     print(" não ta intervalo")

# else:
#     print("esta")


#Q3

# produtos = ['arroz', 'feijao', 'ovo']

# if 'arroz' in produtos:
#     print("Esta na lista")

# else:
#     print('nao')


#Q4


# banidos = ['carlos', 'jao', 'arão']

# usuario = 'arão'

# if usuario not in banidos:
#     print("não está na lista")
# else:
#     print("está na lista")



#Q5

# logado = str(input('digite sim, se estiver logado e não, se n estiver: '))

# suspenso = str(input('diga sim, se esta suspenso e não, se nao esta: '))

# usuario = {
#     'logado': logado,
#     'suspensao': suspenso
# }

# if 'sim' in usuario['logado'] and 'nao' in usuario['suspensao']:
#     print("Bem-vindo!")

# else:
#     print("sai fora")

#Q6

# palavra = str(input())

# if 'a' in palavra:
#     print("Existe 'a' na palavra")
# else:
#     print('nao existe')

#Q7
# idade = 5
# autorizacao = True

# if idade > 18 or autorizacao == True:
#     print("Pode comprar bebida")
# else:
#     print("nao pode")

#Q8
# """Toda lista vazia retorna False"""
# emails = []

# if not emails == '':
#     print('Nenhum e-mail encontrado')
# else:
#     print('tem emails')

#Q9
# lista = ["admin", "root"]
# usuario = 'jao'

# if usuario not in lista:
#     print('Login válido')
# else:
#     print('invalido')


#Q10

# n = 2
# if n%2 == 0 and n > 0:
#     print('par e positivo')
# else:
#     print('impar e provavelmente negativo ou positivo')