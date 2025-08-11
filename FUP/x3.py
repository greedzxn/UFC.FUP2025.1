vetor = []

for i in range(5):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    vetor.append(numero)

print("\nNúmeros pares e suas respectivas posições:")
for posicao, numero in enumerate(vetor):
    if numero % 2 == 0:
        print(f"Número {numero} na posição {posicao}")
