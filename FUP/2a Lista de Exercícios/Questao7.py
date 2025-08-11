#Entrada

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o primeiro número: "))
n3 = float(input("Digite o primeiro número: "))

#Criação de lista de números ímpares

impares = []

#Verificação dos números

if n1%2 !=0:
    impares.append(n1)   

if n2%2 !=0:
    impares.append(n2)

if n3%2 !=0 :
    impares.append(n3)

if not impares:
    print("Não há nenhum número impar!")

else:
    print(f"O maior número ímpar é: {max(impares)}")