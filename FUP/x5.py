vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero > 0:
        vetor.append(numero)

if len(vetor) == 10:
    maior = vetor[0]
    menor = vetor[0]

    for numero in vetor:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    print(f'O maior número positivo digitado foi: {maior}')
    print(f'O menor número positivo digitado foi: {menor}')

else:
    print('Algum número digitado não é positivo!')