numeros = list(range(1,11))

pares = []
impares =[]

for posicao, numero in enumerate (numeros):
    if numero % 2 == 0:
        pares.append((numero, posicao))
    
    else:
        impares.append((numero, posicao))

print(f'Esta é a lista de números pares: {numeros} {posicao}')
print(f'Esta é a quantidade de números pares: {len(pares)}')
print(f'Esta é a lista de números impares: {impares}')
print(f'Esta é a quantidade de números impares: {len(impares)}')