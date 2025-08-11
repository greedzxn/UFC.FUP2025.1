curso = 'Programação em Python'

print(len(curso.replace(" ", '')))
print('prog' in curso)
print(curso.count('i'))
print(curso.count('I'))
print(curso.count('o'))
print(curso.count('O'))
print(curso.find('o'))
print(curso.rfind('o'))

palavra = curso.lower()
palavra = palavra.split(' ')
palavra1 = palavra[2]

print(sorted(palavra1))

palavra2 = curso.replace(' ','_')
palavra3 = palavra2.replace('Python', 'Java')

print(palavra3)