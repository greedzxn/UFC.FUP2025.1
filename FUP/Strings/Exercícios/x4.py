numero = input('Digite o número do seu telefone ')
numero = list(numero)
if len(numero)==7:
    numero.insert(0, '3')

if numero[4] != '-':
    numero.insert(4, '-')
    numero = ''.join(numero)

print(numero)