n1 = float(input("Qual o foi chute do primeiro aluno? "))
chute = input("O valor chutado pelo segundo aluno foi maior ou menor? ").lower()
n2 = float(input("Qual o foi número que o professor pensou? "))

#ALgoritmo

#Possibilidades que o primeiro aluno ganha:
if n1 == n2:
    print("O primeiro aluno ganhou!")

elif  n1 < n2 and chute == "menor":
    print("O primeiro aluno ganhou!")

elif  n1 > n2 and chute == "maior":
    print("O primeiro aluno ganhou!")

#Possibilidades que o segundo aluno ganha:
elif n1 != n2:
    print("O segundo aluno ganhou!")
    
elif  n1 < n2 and chute == "menor":
    print("O segundo aluno ganhou!")

elif  n1 > n2 and chute == "maior":
    print("O segundo aluno ganhou!")
