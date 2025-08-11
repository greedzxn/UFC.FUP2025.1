while True:

    numero = input('Digite o número do seu telefone: ')
    numero = numero.strip()  # Remove espaços em branco extras

    # Verifica se o número tem apenas dígitos
    if not numero.isdigit():
        print("Entrada inválida. Digite apenas números.")
    else:
        break
if len(numero) == 8:
    # Adiciona o 9 no início
    numero = '9' + numero
    
if len(numero) == 9 and numero[0] == '9':
    # Formata como 9 XXXX-XXXX
    numero_formatado = f"{numero[0]} {numero[1:5]}-{numero[5:]}"
    print(numero_formatado)
else:
    print("Número inválido ou em formato inesperado.")
