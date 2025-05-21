#Faça um programa que receba três números e mostre a saída a seguir:
#❖ Entrada:
#Digite o 1o número: 5
#Digite o 2o número: 3
#Digite o 3o número: 2
#❖ Saída:
#O menor número digitado foi: 2
#O maior número digitado foi: 5
#A soma dos números digitados foi: 5 + 3 + 2 = 10

#Entrada dos números

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

#Definição de variáveis

valores = [n1, n2, n3]
menor = min(valores)
maior = max(valores)
soma = n1 + n2 + n3

#Exibição dos resultados
print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}") 
print(f"A soma dos números digitados foi: {n1} + {n2} + {n3} = {soma}")