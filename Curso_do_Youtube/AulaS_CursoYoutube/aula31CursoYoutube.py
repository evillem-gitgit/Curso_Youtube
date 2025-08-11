"""
como encontrar arquivos no sistema
"""
import os

caminho_procura = 'C:/Users/evill/OneDrive/Imagens/Capturas de tela'
termo_procura = 'acai'

conta = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:

        if termo_procura in arquivo:
            try:
                conta += 1

                caminho_completo = os.path.join(raiz, arquivo)

                nome_arquivo, exten_arquivo = os.path.splitext(arquivo)

                tamanho = os.path.getsize(caminho_completo)
                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensao: ', exten_arquivo)
                print('Tamanho: ', tamanho)

            except PermissionError as e:
                print('Sem permissões')

            except FileNotFoundError as e:
                print('Arquivo não encontrado')

            except Exception as e:
                print('Erro desconhecido', e)

print()
print(f'{conta} arquivo(s) encontrado(s).')