#Faça uma função que recebe uma frase e substitui todas as ocorrências de espaço por "#". Faça também uma função para realizar a entrada de dados. 
#A saída de dados deve ser feita no programa principal


def troca(fname):
    frase.strip()
    frase_trocada = ''
    for i in frase:
        if i == ' ':
            i = '#'
        frase_trocada += i

    print(frase_trocada)

frase = input('Digite uma frase: ')
troca(frase)