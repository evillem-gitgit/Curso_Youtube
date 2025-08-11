from datetime import date
anoAtual = date.today().year

anoNasci = int(input('Ano de nascimento:'))

idade = anoAtual - anoNasci

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    idade = anoAtual - anoNasci
    print('Classificação: MIRIM')
    
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')   

elif idade  > 9 and idade <= 19:
    print('Classificação: JUNIOR')

elif idade > 9 and idade <= 25:
    print('Classificação: SêNIOR')

else:
    print('Classificação: MASTER')    



def process(value):
    match value:
        case 1:
            print("É um!")
        case 2:
            print("É dois!")
        case 3 | 4:
            print("É três ou quatro!")
        case _:
            print("Outro valor.")

process(2)
# Saída: É dois!

    