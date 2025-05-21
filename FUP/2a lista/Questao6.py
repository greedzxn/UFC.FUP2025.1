import math

#Menu de Opções

print("Menu de opções")
print("2 - Somar dois números")
print("3 - Dividir dois números")
print("4 - Raiz quadrada de um número")
opcao = int(input("Digite sua opção: "))

#Operações 

if opcao == 2:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resultado = n1+n2
    print(f"A soma dos dois números foi: {resultado:.2f}")

elif opcao == 3:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    if n2 == 0:
        print("O segundo número não pode ser zero!")
    else:
        resultado = n1/n2
        print(f"A divisão dos dois números foi: {resultado:.2f}")

elif opcao == 4:
    n1 = float(input("Digite um número: "))
    if n1 < 0:
        print("O número não pode ser negativo!")
    else:
        resultado = math.sqrt(n1)
        print(f"o resultado da raiz quadrada foi: {resultado:.2f}")

else:
    print("Opção inválida! Digite 2, 3 ou 4.")

