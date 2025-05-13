import math

#Dados do usuário

dados_do_usuario = float(input("Digite o tamanho do arquivo em MB:"))
velocidade = float(input("Digite a velocidade de download em Mbps:"))

#Conversão de Mbps para MBps
velocidade_MBps = velocidade / 8

#Cálculo do download
tempo = dados_do_usuario / velocidade_MBps

#tempo do download em minutos
tempo_minutos = math.ceil(tempo / 60)

#Exibição do resultado

print(f"Tempo de download: {tempo_minutos:.2f} minutos")