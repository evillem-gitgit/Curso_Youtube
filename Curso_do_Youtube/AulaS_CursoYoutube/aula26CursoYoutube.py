""" 
Try, Except
"""


try:
    a = []
    print(a)

# esse 'as' joga oq estiver NameError na variavel erro!    
except NameError as erro:# eu especifiquei o tipo de erro (NameError é erro com nomes)

    print('Esse foi o Erro: ', erro)

# consigo colocar dois tipos <:
except (IndexError, KeyError) as erro:
    print("Erro de indice amor")


# ele pega qualquer erro q der
except Exception as error:# Exception é qualquer outro erro alem do NameError
    print('Ocorre um erro inesperado')

else:
    print('Seu codigo não deu nehum desses erro ai')



print("continua esse codigo")