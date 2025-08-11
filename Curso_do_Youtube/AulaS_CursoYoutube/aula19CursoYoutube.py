"""
Trocando valor entre variaveis"""

x = 10
y = 'Luiz'
print(f'X = {x} e Y = {y}\n')

x, y = y, x # trocando os valores
print(f'Com valores trocado: ')
print(f' X = {x} e Y = {y}')