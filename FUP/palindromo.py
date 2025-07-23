def palindromo(palavra):
    palavra = palavra.replace(' ', '').lower()
    return palavra == palavra[::-1]

palavra = input('Digite uma palavra qualquer: ')

if palindromo(palavra):
    print("Esta palavra é um palíndromo")

else:
    print("Esta palavra não é um palíndromo")