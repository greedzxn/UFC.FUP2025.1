#Input para cálculo do fatorial
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1 #Aqui assumimos que o fatorial de 1 é 1 (1!=1)

#Sequência que calcula o fatorial do número pedido anteriormente
for i in range(1, numero + 1):
    fatorial = fatorial * i

print(f"O fatorial de {numero} é {fatorial}")   