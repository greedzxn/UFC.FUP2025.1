#Quantidade de Quilos de peixe que João pescou

peixes = float(input("Digite a quantidade de quilos de peixe que João pescou: "))

#Cálculo do excesso

excesso = peixes - 50
if excesso > 0:
    multa = excesso * 4
else:
    multa = 0

#Exibição do resultado
print(f"João pescou {peixes} quilos de peixe.")
print(f"Excesso: {excesso} quilos.")
print(f"Multa: R$ {multa:.2f}")