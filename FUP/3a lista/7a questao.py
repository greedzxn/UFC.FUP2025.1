pais_A = 80000
pais_B = 200000

while pais_A <= pais_B:
    pais_A += pais_A*0.03
    pais_B += pais_B*0.015
    anos += 1

print(f'Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B')