#Função para traduzir uma única base
def traduzir_base(base):
    if base == "A":
        return "T"
    elif base == "U":
        return "A"
    elif base == "C":
        return "G"
    elif base == "G":
        return "C"
    else:
        return "Base inválida!"

# Receber as bases do usuário
base1 = input("Insira a primeira base nitrogenada: ").upper()
base2 = input("Insira a segunda base nitrogenada: ").upper()
base3 = input("Insira a terceira base nitrogenada: ").upper()

# Traduzir cada base
dna1 = traduzir_base(base1)
dna2 = traduzir_base(base2)
dna3 = traduzir_base(base3)

# Resultado
print(f"As bases nitrogenadas no ADN são: {dna1} {dna2} {dna3}")
