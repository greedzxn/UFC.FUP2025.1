#Entrada da variáveis
preco = float(input('Qual o valor original da compra? '))
desconto = float(input('Qual o valor do desconto? '))
leao =  float(input('Qual o valor do imposto? '))

#Cálculo do Algoritmo
preco_com_desconto = preco-(preco*(desconto/100))
preco_com_imposto = preco_com_desconto+(preco_com_desconto*(leao/100))

#Resultado
print(f'O valor final da compra é R$ {preco_com_imposto:.2f}')    
