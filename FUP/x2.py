numeros = []
i = 1

while i <=5:
    numeros.append(i)
    i+=1

print('Números pares e suas posições: ')
tem_par = False
for posicao, numero in enumerate(numeros):
    if numero%2 ==0:
        print (f'Número {numero} na posição {posicao}')

    if not tem_par:
        print('Não há números pares na lista')