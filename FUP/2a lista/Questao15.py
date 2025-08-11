#Entrada de dados
salario_min = float(input('Qual o valor do salário mínimo? '))
salario_func = float(input('Qual o valor do salário do funconário? '))

#Cálculo algoritmo
quantidade_salarios = salario_func//salario_min

#Resultado
print(f'A quantidade de salários mínimos que esse funcionário recebe é: {quantidade_salarios:.2f}')
