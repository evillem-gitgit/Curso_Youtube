"""
🗂️ 2. Cadastro de Produtos com Verificação de Dados
Contexto:
Em um sistema de gerenciamento de estoque, os funcionários
devem poder cadastrar produtos.

Desafio:
Crie um sistema que:

Cadastre novos produtos com nome, preço e quantidade.

Verifique se os dados são válidos (por exemplo, preço e quantidade não podem ser negativos).

Armazene tudo em uma lista de dicionários.
"""
import openpyxl



nome = str('digite o nome do produto: ')
preco = float('digite o preço do produto: ')
qtd = int('digite a quantidade de produto no estoque: ')


produtos = {
    'Produto':{
        'nome': nome,
        'preco': preco,
        'quantidade': qtd
    }
}



for indice, (produto, dados) in enumerate(produtos.items()):
    print(f'\n {indice}. {produto}')

    for dado in dados.items():
        print(dado)
