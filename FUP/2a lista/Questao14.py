#variáveis
dolar = 5.67
alemao = 3.25
libra = 7.5380

#entradada de dados
dinheiro = float(input('Qual a quantidade de dinheiro que você possui? (em reais)'))

#algoritmo

conversao_dolar = dinheiro/dolar
conversao_alemao = dinheiro/alemao
conversao_libra = dinheiro/libra

#Resultado

print(f'R$ {dinheiro} são ${conversao_dolar:.2f} dólares')
print(f'R$ {dinheiro} são DM{conversao_alemao:.2f} marcos alemãos')
print(f'R$ {dinheiro} são £{conversao_libra:.2f} libras')
