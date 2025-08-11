# matriz = [       '0'          '1'           '2'
#                'coluna'     'coluna'     'coluna'
#     'linha > 0' [  1,          2,           3],
#     'linha > 1' [  4,          5,           6],
#     'linha > 2' [  7,          8,           9]
# ]
#          #linha     #coluna
# print(matriz[2]    [1])

# m, n = map(int, input(). split())
# # m - numero de linhs
# # n - numero de colunas


# matriz = [[0] * n] * m

# for x in matriz:

#     for y in x:
#         print(y, end='')
#     print()

# for x in [[0,0,0], [0,0,0]]:
#     for y in x:
#         pass


# matriz = []
# for _ in range(m):
#     string = input()
#     matriz.append(string)
# print(matriz)



n, m = map(int, input(). split())

matriz = [[0] * n] * m

for _ in range(n):
    string = input()
    matriz.append(string)
print(matriz)