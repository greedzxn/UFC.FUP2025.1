a = 1
b = 1

i = int(input('A série irá até qual termo? '))

print(f'Veja a seguir a série até o {i}° termo')

print(f'{a}/{b}')

for i in range(i):
    a += 1
    b += 2
    print(f'{a}/{b}')
