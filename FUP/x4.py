vetor = []
#primo = []
#primos = True

for i in range(9):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    vetor.append(numero)

#for n in range(2, int(numero**0.5) + 1):
    #if numero % n == 0:
        #primos = False
        #break


print("\nNúmeros primos e suas respectivas posições:")
for posicao, numero in enumerate(vetor):
    if 10/2==5:
        print(f"Número {numero} na posição {posicao+1}")


