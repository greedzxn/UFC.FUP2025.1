# Inicializa contadores
candidato_um = 0
candidato_dois = 0
candidato_tres = 0
candidato_quatro = 0
votos_nulos = 0
votos_branco = 0
total_votos = 0

# Exibe o menu de opções
print('\nMenu de votação:')
print('1 - Candidato Um')
print('2 - Candidato Dois')
print('3 - Candidato Três')
print('4 - Candidato Quatro')
print('5 - Voto Nulo')
print('6 - Voto em Branco')
print('0 - Encerrar votação')

# Loop para entrada dos votos
while True:
    voto = int(input('Digite seu voto: '))
    
    if voto == 0:
        break  # condição de parada
    elif voto == 1:
        candidato_um += 1
    elif voto == 2:
        candidato_dois += 1
    elif voto == 3:
        candidato_tres += 1
    elif voto == 4:
        candidato_quatro += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print('Voto inválido! Tente novamente.')
    
    total_votos += 1

#Evita divisão por zero
if total_votos == 0:
    print('\nNenhum voto foi registrado.')
    
else:
    # Calcula as porcentagens
    porcentagem_um = candidato_um * 100 / total_votos
    porcentagem_dois = candidato_dois * 100 / total_votos
    porcentagem_tres = candidato_tres * 100 / total_votos
    porcentagem_quatro = candidato_quatro * 100 / total_votos
    porcentagem_nulo = votos_nulos * 100 / total_votos
    porcentagem_branco = votos_branco * 100 / total_votos

    # Exibe o resultado
    print('\nResultado da eleição:')
    print(f'Candidato 1: {candidato_um} votos ({porcentagem_um:.2f}%)')
    print(f'Candidato 2: {candidato_dois} votos ({porcentagem_dois:.2f}%)')
    print(f'Candidato 3: {candidato_tres} votos ({porcentagem_tres:.2f}%)')
    print(f'Candidato 4: {candidato_quatro} votos ({porcentagem_quatro:.2f}%)')
    print(f'Votos nulos: {votos_nulos} votos ({porcentagem_nulo:.2f}%)')
    print(f'Votos em branco: {votos_branco} votos ({porcentagem_branco:.2f}%)')
