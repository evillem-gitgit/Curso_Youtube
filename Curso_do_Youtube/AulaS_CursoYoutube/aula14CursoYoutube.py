"""
Desempacotamento de listas"""
# lista = ['luiz', 'joao', 'maria',1,2,3,4,5,6,7,9,100]

# n1, n2, n3 = lista #!DESSA FORMA DA ERRO POIS...
# print(n1, n2, n3)  # A MAIS VALORES PARA SER DESEMPACOTADOS DO Q
                   #VARIAVEIS


# lista = ['luiz', 'joao', 'maria',1,2,3,4,5,6,7,9,100]
# n1, n2, n3, *outra_lista = lista  #ele cria outra lista com o                 
#                                   # restante da lista
# print(n1, n2, n3, outra_lista)    



lista = ['luiz', 'joao', 'maria',1,2,3,4,5,6,7,9,100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista                
                                  
print(n1, n2, n3, ultimo_da_lista)
