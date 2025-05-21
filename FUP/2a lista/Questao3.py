#Exercício:
#Leia 3 valores Inteiros. A seguir mostre quantos valores digitados foram
#pares, quantos valores digitados foram ímpares, quantos valores
#digitados foram positivos e quantos valores digitados foram negativos.

#Definição de itens pares, ímpares, positivos e negativos

par = 0
impar = 0
positivo = 0
negativo = 0

#Entrada dos números

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite o último número inteiro: "))

#Classificação dos números

#Primeiro Número
if n1 >0:
    positivo +=1
elif n1<0:
    negativo += 1
else:
    print("O primeiro número digitado é zero")

if n1%2 == 0:
    par +=1
else:
    impar +=1

#Segundo Número
if n2 >0:
    positivo +=1
elif n2<0:
    negativo += 1
else:
    print("O segundo número digitado é zero")

if n2%2 == 0:
    par +=1
else:
    impar +=1

#Terceiro Número
if n3 >0:
    positivo +=1
elif n3<0:
    negativo += 1
else:
    print("O terceiro número digitado é zero")

if n3%2 == 0:
    par +=1
else:
    impar +=1

#Exibição dos resultados:

print(f"{par} valor(es) par")
print(f"{impar} valor(es) impares")
print(f"{positivo} valor(es) positivos")
print(f"{negativo} valor(es) negativos")