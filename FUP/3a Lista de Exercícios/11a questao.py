a = int(input('Digite um valor inteiro '))
b = int(input('Digite um valor inteiro '))

if type(a) and type(b) == int:
    if a % b == 0 or b % a == 0:
        print('Eles são múltiplos')
    else:
        print('Eles não são múltiplos')