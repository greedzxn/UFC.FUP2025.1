import math

#Entrada

nome_funcionario = input("Digite o nome do funcionário: ")
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor total das vendas: "))

#Cálculo da comissão
comissao = vendas * 0.15
comissao_total = comissao + vendas
salario_total = salario_fixo + comissao_total

#Exibição do resultado
print(f"O Funcionário {nome_funcionario} ganhou um total de R$ {salario_total:.2f} esse mês!")