# Solicita ao usuário quantos termos deseja ver
n = int(input("Digite o número de termos da sequência: "))

# Inicializa variáveis de controle
grupo = 0  # número do grupo
termos_gerados = 0  # contador de quantos termos já mostramos

# Gera os termos enquanto não atingimos o total desejado
while termos_gerados < n:
    grupo += 1
    a = 2 ** grupo
    b = a * 3 + 1
    c = a * 3 + 3

    # Exibe os termos do grupo, mas só se ainda não ultrapassou N
    for termo in [a, b, c]:
        if termos_gerados < n:
            print(termo, end=', ')
            termos_gerados += 1