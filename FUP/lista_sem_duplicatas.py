def remover_duplicados(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

def preencher_lista():
    lista = []
    print("Adicione o item a lista(digite 'fim' para encerrar)")
    while True:
        item = input('Item a ser adicionado: ')        

        if item.lower() == 'fim':
            break
        lista.append(item)
    return lista

if __name__ == "__main__":
    lista = preencher_lista()
    lista_sem_duplicatas = remover_duplicados(lista)
    print(lista)
    print(lista_sem_duplicatas)

                                              
