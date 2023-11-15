def remove_repetidos(lista):
    lista.sort()
    lista_nova = []
    lista_nova.append(lista[0])
    for x in range(1,len(lista)):
        if lista[x] != lista[x - 1]:
            lista_nova.append(lista[x])
    return lista_nova












