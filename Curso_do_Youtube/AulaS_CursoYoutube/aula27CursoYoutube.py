"""
Para que serve o raise?
Criar seus próprios erros

Interromper o código quando algo inesperado acontece

Informar ao usuário ou desenvolvedor o que está errado


"""
# exemplo 1

# def divide(n1, n2):

#     try:
#         return n1/n2
        
#     except ZeroDivisionError as erro:
#         print('Não pode dividir nada por zero boco')
#         print(erro)
#         raise# ele ta repassando esse erro de divisão para o outro try tbm

# try:
#     print(divide(2,0))

# except ZeroDivisionError as erro:
#     print(erro)












# exemplo 2


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser zero")
    return n1/n2


try:
    print(divide(2,0))

except ValueError as erro:
    print(erro)