i = input('Qual a sua data de nascimento? ')
a = i.split('/')

if a[-2] == '01':
    a[1:2] = ['Janeiro']

elif a[-2] == '02':
    a[1:2] = ['Fevereiro']

elif a[-2] == '03':
    a[1:2] = ['Março']

elif a[-2] == '04':
    a[1:2] = ['Abril']

elif a[-2] == '05':
    a[1:2] = ['Maio']

elif a[-2] == '06':
    a[1:2] = ['Junho']

elif a[-2] == '07':
    a[1:2] = ['Julho']

elif a[-2] == '08':
    a[1:2] = ['Agosto']

elif a[-2] == '09':
    a[1:2] = ['Setembro']

elif a[-2] == '10':
    a[1:2] = ['Outubro']

elif a[-2] == '11':
    a[1:2] = ['Novembro']

elif a[-2] == '12':
    a[1:2] = ['Dezembro']

print(f'Você nasceu no dia {a[0]} de {a[1]} de {a[2]}')