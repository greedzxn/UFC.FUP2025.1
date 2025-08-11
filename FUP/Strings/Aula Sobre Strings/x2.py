i = input('Digite uma palavra qualquer: ').lower()


while len(i)>0 and i[0] == 'ç' and i[1] == 'ç':
    i = i[1:]

if i.startswith('ç'):
    i = 's' + i[1:]

while len(i)>0 and i[0] == 's' and i[1] == 's':
    i = i[1:]

print(i)