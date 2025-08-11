"""
Geradores, iteradores e iteráveis

hasattr(variavel, '__iter__') - Essa função ai serve pra vc verificar
se uma variavel é iteravel

"""
import sys



lista1 = [x for x in range(10000)]# lista salva na memoria
lista2 = (x for x in range(10000))# n salva na memoria

print(sys.getsizeof(lista1),'bits de memoria')
print(sys.getsizeof(lista2),'bits de memoria')




# lista = list(range(6))
# print(lista)

# lista = [0, 1, 2, 3, 4, 5]
# print(hasattr(lista, '__iter__'))
# #     Essa função ai serve pra vc verificar se a lista é iteravel


# lista2 = 123
# print(hasattr(lista2, '__iter__'))

# lista3 = 'string'
# print(hasattr(lista3, '__iter__'))







# lista = [0, 1, 2, 3, 4, 5]
# print(hasattr(lista, '__next__'))
# #     Essa função é pra saber se é um iterador



"""
def contar_ate_tres():
    yield 1
    yield 2
    yield 3
#Chamando essa função:

for numero in contar_ate_tres():
    print(numero)
#🔹 Saída:

#1
#2
#3
#A função contar_ate_tres não
#  etorna todos os valores de uma vez,
# ela entrega um por vez quando o for ou next() pede.

"""