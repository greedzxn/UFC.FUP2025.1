#Entrada de dados
ap1 = float(input('Qual a nota do aluno na primeira prova? '))
ap2 = float(input('Qual a nota do aluno na segunda prova? '))

#Definição de nota mais alta e mais baixa
num = [ap1, ap2]
num.sort()

#Cálculo o algoritmo
nota_mais_baixa = num[0]*2
nota_mais_alta = num[1]*1

nota_final = (nota_mais_alta+nota_mais_baixa)/3

#Resultados
if nota_final <= 4 and nota_final >= 0:
    print('Reprovado')

elif nota_final > 4:
    print('Aprovado')
