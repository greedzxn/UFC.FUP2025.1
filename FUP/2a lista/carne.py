#Contagem de estrelas

estrelas = 0

#Verificação do Prazo de Validade

validade = input ("A carne ainda está dentro do prazo de validade? ").lower()

if validade !="sim":
    print("A carne está fora de validade, e portanto, reprovada no teste")
    

else: 
    # Adição de uma estrela por estar na validade
    estrelas += 1
    # Demais perguntas
    gordura = input ("A carne está com gordura branca e firme? ").lower()
    if gordura == "sim":
       estrelas += 1

    cor = input ("A carne possui cor vermelho-brilhante? ").lower()
    if cor == "sim":
        estrelas += 1
    
    temperatura = input ("A carne está em uma temperatura inferior a 7 graus? ").lower()
    if temperatura == "sim":
        estrelas += 1

    cheiro =input ("A carne possui cheiro agradável? ").lower()
    if cheiro == "sim":
        estrelas += 1

        if estrelas > 3:
         print(f"A carne recebeu {estrelas} estrelas, e portanto, passou no teste")
        else:
         print(f"A carne recebeu {estrelas} estrelas e portanto, não passou no teste")
#Resultados


