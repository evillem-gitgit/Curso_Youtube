import os
import shutil

"""
os.walk() serve para percorrer todas as pastas,
subpastas e arquivos dentro de um diretório(pasta)
"""



caminho_original = 'C:/Users/evill/OneDrive/Imagens/Capturas de tela'
#!!!!!
"""caminho_original: cria uma variável chamada caminho_original que guarda
o caminho (string) da pasta onde estão os arquivos que você quer ler."""




caminho_pasta_novo = 'C:/Users/evill/OneDrive/Imagens/Capturas de telaTeste'
#!!!!!!
""" caminho_pasta_novo: cria outra variável com o caminho da
pasta de destino (onde você quer colocar/copiar/mover os arquivos)."""





try:
    os.mkdir(caminho_pasta_novo)#criar uma nova pasta

# Se a pasta criada ja existir... já sabe né

except FileExistsError as erro:
    print(f'pasta {caminho_pasta_novo} ja existe.')

for root, dirs, files in os.walk(caminho_original):
    """
    -Usa os.walk() para percorrer a pasta caminho_original 
    recursivamente (ou seja, também entra em subpastas!).

    -A cada iteração os.walk devolve três coisas:
    *root: o caminho da pasta atual que está sendo visitada,
    *dirs: lista de subpastas dentro de root (pode ser ignorada se você só quer arquivos),
    *files: lista de nomes de arquivo (strings) dentro de root.
    """

    for file in files:
        caminho_antigo = os.path.join(root, file)

        """
        - junta o caminho da pasta atual (root) com
        o nome do arquivo (file) para formar o caminho
        completo do arquivo original

        - os.path.join cuida de barras corretamente.
        """

        new_caminho_arquivo = os.path.join(caminho_pasta_novo, file)

    ##esta movendo o antigo para o novo caminho
        shutil.move(caminho_antigo, new_caminho_arquivo)
        print(f'Arquivo {file} movido com sucesso!')