#Criação de variáveis para validação dos votos

candidato_um = 0
candidato_dois = 0
candidato_tres = 0

#Validação do número de eleitores
i = int(input('Quantos eleitores irão votar? '))

#Menu para informar eleitores
print('\nMenu')
print('Selecione uma opção para cada voto')
print('1 - Candidato Um')
print('2 - Candidato Dois')
print('3 - Candidato Três')

#Algoritmo de validação dos votos
for j in range(0,i):
    while True:
        voto = int(input(f'Qual o voto do {i+1}° eleitor? '))
        if voto == 1:   
            candidato_um += 1
            break
        elif voto == 2:
            candidato_dois += 1
            break
        elif voto == 3:
            candidato_tres += 1
            break
        else:
            print('Digite um número válido')

#Exibição dos votos
print(f'\nResultado da eleição:')
print(f'Candidato Um: {candidato_um} voto(s)')
print(f'Candidato Dois: {candidato_dois} voto(s)')
print(f'Candidato Três: {candidato_tres} voto(s)')