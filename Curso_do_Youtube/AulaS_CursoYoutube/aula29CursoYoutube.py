

#quando vc quer uma constante em python vc escreve a variavel em maiusculo

def valor_PI():
    import math       
    PI = math.pi
    return PI


def dobrar_lista(lista):
    return [x*2 for x in lista]



def multiplicar(lista):
    r = 1
    for i in lista:
        r = r * i
    return r
