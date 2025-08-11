#Define os dois primeiros termos da sequência (1 e 2)
a = 1
b = 2

#Solicita ao usuário até qual termo da sequência ele deseja ver
i = int(input('A série de Fibonacci irá até qual termo? '))

#Exibição de mensagem informando até qual termo a sequência será mostrada
print(f'Veja a seguir a série de Fibonacci até o {i}° termo')

#Exibe os dois primeiros termos (1 e 2)
print(a , b)

#Executa o loop para calcular e mostrar os próximos termos
#Como já mostramos 2 termos, precisamos calcular (i - 2) termos restantes
for i in range(i - 2):
    c = a + b        # Soma dos dois termos anteriores (regra da sequência)
    print(c)         # Exibe o novo termo
    a = b            # Atualiza o valor de 'a' para o próximo passo
    b = c            # Atualiza o valor de 'b' para o próximo passo
