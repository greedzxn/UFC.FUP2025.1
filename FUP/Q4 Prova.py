#Menu de opções
print("Menu de opções")
print("1 - Limpeza")
print("2 - Alimentação")
print("3 - Vestuário")

#Entrada
categoria = int(input("Qual a categoria do produto? "))
preco = float(input("Qual o preço do produto? "))
refrigeracao = input("O Produto precisa de refrigeração? ").lower()

#Algoritmo sobre valor do aumento

#Algoritmo se o preço do produto for menor do que R$ 25,00
if preco <= 25:
    if categoria == 1:
        preco = preco+(preco*0.05)
        print(f"O valor do produto com o aumento é: R$ {preco:.2f}")

    elif categoria == 2:
        preco = preco+(preco*0.08)
        print(f"O valor do produto com o aumento é: R$ {preco:.2f}")

    elif categoria == 3:
        preco = preco+(preco*0.1)
        print(f"O valor do produto com o aumento é: R$ {preco:.2f}")

    else:
        print(f"Erro: não foi digitado uma opção válida!")

#Algoritmo se o preço do produto for maior do que R$ 25,00
elif preco > 25:
     if categoria == 1:
        preco = preco+(preco*0.12)
        print(f"O valor do produto com o aumento é: R$ {preco:.2f}")

     elif categoria == 2:
        preco = preco+(preco*0.15)
        print(f"O valor do produto com o aumento é: R$ {preco:.2f}")

     elif categoria == 3:
        preco = preco+(preco*0.18)
        print(f"O valor do produto com o aumento é: R$ {preco:.2f}")

     else:
        print(f"Erro: não foi digitado uma opção válida!")


#ALgoritmo sobre valor do imposto
if categoria == 2 and refrigeracao == "sim":
    preco = (preco*0.08)
    print(f"O valor do imposto será de: R$ {preco:.2f}")

else:
    preco = (preco*0.05)
    print(f"O valor do imposto será de: R$ {preco:.2f}")
