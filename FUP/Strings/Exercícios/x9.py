lista1 = int(input('Qual a quantidade de peixes no aquário? '))
lista2 = []

for i in range(lista1):
    peixes = input(f'Qual a espécie do {i+1}º peixe? ').upper()
    if peixes not in lista2:
        lista2.append(peixes)

print(f' {len(lista2)} é a quantidade de diferentes espécies de peixes existentes no aquário ')