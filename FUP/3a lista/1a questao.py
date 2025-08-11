#Variáveis
pares = 0
impar = 0
zero = 0

#EStrutura de repetição para cálculo de variáveis
for i in range(0,10):
    numero = int(input('Digite um número inteiro: '))

    if numero == 0:
        zero += 1
    elif numero % 2 == 0:
        pares += 1
    else:
        impar += 1

#Exibição de Resultados
print(f'Esta é a quantidade de números pares: {pares}')
print(f'Esta é a quantidade de números impares: {impar}')
print(f'Foi digitado um total de {zero} zeros')