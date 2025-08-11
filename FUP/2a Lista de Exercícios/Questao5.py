#Entrada

tempo = float(input("Qual foi o tempo da viagem (em horas)? "))
velocidade = float(input("Qual foi a velocidade média do veículo (em km/h)? "))

#Declaração das variáveis

consumo_por_litro = 12
distancia = tempo*velocidade

#Cálculo

combustível = distancia/consumo_por_litro

#Saída

print(f"A quantidade necessária de combustível é: {combustível:.3f} litros")