palavra = input('Digite uma palavra ')
codigo = ''
for i in palavra:
        if i == 'a' or i == 'A':
                i = '4'
        if i == 'o' or i == 'O':
                i = '*'
        if i == 's' or i == 'S':
                i = '5'
        codigo += i

print(codigo)