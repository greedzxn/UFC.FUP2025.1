soma = 0
media = 0

for i in range(0,5):
    num = int(input('Digite um número inteiro '))
    soma += num
    media = soma/(i+1)

print(f'A soma dos números digitado foi: {soma}')
print(f'A média dos números digitado foi: {media}')
