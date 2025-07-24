def criar_arquivo(arquivo):   
    arquivo = open(arquivo, 'wt')
    i = 101
    while i <=1000:
        arquivo.write(f'{i}. \n')
        i+=1

    arquivo.close()

def ler_arquivo(arquivo):
    arquivo = open(arquivo, "rt")
    print(arquivo.read())
    arquivo.close()
    
arquivo = "C:/Users/582775/Documents/numeros.txt"
criar_arquivo(arquivo)
ler_arquivo(arquivo)