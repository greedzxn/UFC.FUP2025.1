ano = int(input('Qual ano você deseja verificar se é bissexto ou não? '))

bissexto = False
ano = ano*365

if ano % 400 == 0:
    bissexto = True

if ano % 100 == 0:
    bissexto = False

if ano % 4 == 0:
    bissexto = True
else:
    bissexto = False

if bissexto:
    print('Ele é bissexto')
else:
    print('Ele não é bissexto')