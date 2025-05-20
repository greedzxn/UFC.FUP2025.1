import math

# Lê os três valores de ponto flutuante
A, B, C = map(float, input("Digite três valores separados entre espaços").split())

# Calcula as áreas
area_triangulo = (A * C) / 2
area_circulo = math.pi * C ** 2
area_trapezio = ((A + B) * C) / 2
area_quadrado = B ** 2
area_retangulo = A * B

# Exibe os resultados com 3 casas decimais
print(f"Triângulo: {area_triangulo:.3f}")
print(f"Círculo: {area_circulo:.3f}")
print(f"Trapézio: {area_trapezio:.3f}")
print(f"Quadrado: {area_quadrado:.3f}")
print(f"Retângulo: {area_retangulo:.3f}")