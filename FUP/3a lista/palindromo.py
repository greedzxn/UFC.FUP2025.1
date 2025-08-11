def palindromo(palvra):
    palavra = palavra.replace(' ', '').lower()
    return palavra == palavra[::-1]

palavra = input('Digite uma palavra ')

if palindromo:
    print("Esta palavra é um palíndromo")

else:
    print("Esta palavra não é um palíndromo")