frase = input("Digite uma frase: ")
frase = frase.strip() # Remove espaços em branco extras
frase = frase.split() #Separa cada palavra da frase
print(f' A quantidade de palavras na frase é {len(frase)} palavras')