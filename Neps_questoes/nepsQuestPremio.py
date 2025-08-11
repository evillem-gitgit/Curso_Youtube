N = int(input())

soma_acessos = 0

dias = 0

for i in range(N):

    acessos = int(input())

    soma_acessos = soma_acessos + acessos

    dias = dias + 1

    if soma_acessos >= 1_000_000:
        break

# Exibe o número de dias necessários
print(dias)


