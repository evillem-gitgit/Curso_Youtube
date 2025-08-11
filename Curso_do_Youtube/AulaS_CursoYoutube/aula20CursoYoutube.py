from openpyxl import load_workbook


"""
AULA - 20
DICIONARIOS
"""
# EXEMPLO 1

# dicionario = {'chave1' : 'valor da chave'}

# dicionario['nova_chave'] = 'Valor da nova chave'# Adicionando uma nova
#                                                 # chave no dicionario
# print(dicionario)












# EXEMPLO2
# outra forma de criar um dicionario

# dicio = dict(chave1 = 'valor da chave', chave2 = 'valor da chave')
# print(dicio)












# EXEMPLO3

# d1 = {
#     'str': 'valor',
#     123 : 'outro valor',
#     (1,2,3,4): 'tupla',
# }


# # Ao invez de dar erro! quando usa-se o get
# # ele retorna  None


# if d1.get('strs') is None:# se d1 não tem strs ele vai retornar None
#     print('não existe')   # se retornar None print(não existe)

# print('avee')

# if d1.get('str') is not None:# se d1 n tem strs ele vai retornar None
#     print('existe')   # se Não retornar None, então é pq existe












# EXEMPLO 3 CASO QUEIRA APAGAR ALGUM ELEMENTO

# dic = {
#     'str': 'valor',
#     123 : 'outro valor',
#     (1,2,3,4): 'tupla',
# }

# del dic[123]
# print(dic)

# # Como ver o valor nas chaves

# print('str' in dic) #vendo pela chave
# print('str' in dic.keys()) #vendo se a chave str existe no dic
# print('valor' in dic.values()) #vendo pelo valor














# EXEMPLO 4

# dicio = {
#     'str': 'valor',
#     123 : 'outro valor',
#     (1,2,3,4): 'tupla',
# }
# print(dicio)

# # como TROCAR O NOME da chave:
# #dicio['nova_chave'] = dicio.pop('str')

# print()

# for k in dicio:
#     print(dicio[k])  # isso imprime o valor associado à chave k

# for valor in dicio.values():
#     print(valor)


"""
   Método:          O que retorna:	                Exemplo:
dicio.keys()	|  Só as chaves	                    | 'nome', 'idade', 'cidade'
dicio.values()	|  Só os valores	                | 'Ana', 25, 'SP'
dicio.items()	|  Pares (chave, valor) como tuplas | ('nome', 'Ana'), etc.
"""
 











# EXEMPLO 5
# clientes = {
#     'cliente1': {
#         'nome1': 'kayque',
#         'sobrenome1': 'Otávio',
#     },

#     'cliente2': {
#         'nome2': 'jao',
#         'sobrenome2': 'viado',
#     },
# }

# for cliente_k, cliente_v in clientes.items():
#     print(f'Exibindo: {cliente_k}')

#     for dados_k, dados_v in cliente_v.items():
#         print(f'\t{dados_k} = {dados_v}')



# lista = [
#     ['c1', 1],
#     ['c2', 2],
#     ['c3', 3],
# ]

# dicio = dict(lista)
# print(dicio)









"""
atividade
chatzinho
"""
# estoque = [
#     {"nome": "Farinha", "quantidade": 4, "minimo": 10},
#     {"nome": "Ovos", "quantidade": 20, "minimo": 15},
#     {"nome": "Fermento", "quantidade": 2, "minimo": 5},
#     {"nome": "Açúcar", "quantidade": 12, "minimo": 10},
#     {"nome": "Leite", "quantidade": 1, "minimo": 8}
# ]

# for ingrediente in estoque:
#     if ingrediente['quantidade'] < ingrediente["minimo"]:
#         print(f"- {ingrediente['nome']}: temos {ingrediente['quantidade']},")
#         print(f"mínimo recomendado é {ingrediente['minimo']}.")










    