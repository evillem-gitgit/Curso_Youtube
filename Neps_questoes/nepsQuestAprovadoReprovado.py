A, B = map(float, input().split())
# split é para escrever na mesma linha e
#  o map é para converter str para número

media = float((A + B)/2)

if media >= 7:
    print("Aprovado")
    
elif media >= 4:
    print("Recuperacao")
    
else:
    print("Reprovado")