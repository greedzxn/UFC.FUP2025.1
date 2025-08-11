#Entrada

num = int(input("Digite um valor em reais: "))
num2 = num

#Algoritmo de verificação

if 0 < num2 < 1000000:
#calcula a quantidade de cédulas de 100 reais necessárias
    nota100 = num2 // 100
    num2 = num2 % 100

#calcula a quantidade de cédulas de 50 reais necessárias
    nota50 = num2 // 50 
    num2 = num2 % 50

#calcula a quantidade de cédulas de 20  reais necessárias
    nota20 = num2 // 20
    num2 = num2 % 20

#calcula a quantidade de cédulas de 10 reais necessárias
    nota10 = num2 // 10
    num2 = num2 % 10

#calcula a quantidade de cédulas de 5 reais necessárias
    nota5 = num2 // 5
    num2 = num2 % 5

#calcula a quantidade de cédulas de 2 reais necessárias
    nota2 = num2 // 2
    num2 = num2 % 2

#calcula a quantidade de cédulas de moedas de 1 real necessárias
    nota1 = num2 // 1
    num2 = num2 % 1
    
#Resultado    
    print(f"O valor digitado foi {num} reais, isso equivale a:")
    print(f"{nota100} nota(s) de R$ 100,00")
    print(f"{nota50} nota(s) de R$ 50,00")
    print(f"{nota20} nota(s) de R$ 20,00")
    print(f"{nota10} nota(s) de R$10,00")
    print(f"{nota5} nota(s) de R$5,00")
    print(f"{nota2} nota(s) de R$2,00")
    print(f"{nota1} moeda(s) de R$1,00")

else:
    print("Valor deve ser 0 < N < 1000000")




