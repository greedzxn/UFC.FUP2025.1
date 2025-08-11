palavra1 = input('Digite uma palavra ').upper()
palavra2 = input('Digite outra palavra ').upper()
palavra1 = list(palavra1)
palavra2 = list(palavra2)

if len(palavra1) == len(palavra2):
    palavra1.sort()
    palavra2.sort()
    if palavra1 == palavra2:
        print('As duas palavras são anagramas uma das outras')

    else:
        print('As duas palavras não são anagramas')