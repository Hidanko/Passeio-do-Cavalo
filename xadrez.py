m = [[-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1]]
l = []

# caso retorne lista vazia = sem saida
def recursivo(x, y, matriz, lista):
    lista_len = len(lista)
    print (lista_len)
    if len(lista) > 63:
        return lista.copy()

    # caso passe as verificações, atribuir na matriz
    lista.append(x * 10 + y)
    matriz[x][y] = lista_len
	
    lista_resposta = []
    if x - 1 >= 0 and y + 2 <= 7:
        if matriz[x - 1][y + 2] < 0:
            m1 = matriz.copy()
            lista_resposta.append(recursivo(x - 1, y + 2, m1, lista.copy()))
    if x - 1 >= 0 and y - 2 >= 0:
        if matriz[x - 1][y - 2] < 0:
            m2 = matriz.copy()
            lista_resposta.append(recursivo(x - 1, y - 2, m2, lista.copy()))
    if x + 1 <= 7 and y + 2 <= 7:
        if matriz[x + 1][y + 2] < 0:
            m3 = matriz.copy()
            lista_resposta.append(recursivo(x + 1, y + 2, m3, lista.copy()))
    if x + 1 <= 7 and y - 2 >= 0:
        if matriz[x + 1][y - 2] < 0:
            m4 = matriz.copy()
            lista_resposta.append(recursivo(x + 1, y - 2, m4, lista.copy()))
    if x - 2 >= 0 and y - 1 >= 0:
        if matriz[x - 2][y - 1] < 0:
            m5 = matriz.copy()
            lista_resposta.append(recursivo(x - 2, y - 1, m5, lista.copy()))
    if x + 2 <= 7 and y - 1 >= 0:
        if matriz[x + 2][y - 1] < 0:
            m6 = matriz.copy()
            lista_resposta.append(recursivo(x + 2, y - 1, m6, lista.copy()))
    if x - 2 >= 0 and y + 1 <= 7:
        if matriz[x - 2][y + 1] < 0:
            m7 = matriz.copy()
            lista_resposta.append(recursivo(x - 2, y + 1, m7, lista.copy()))
    if x + 2 <= 7 and y + 1 <= 7:
        if matriz[x + 2][y + 1] < 0:
            m8 = matriz.copy()
            lista_resposta.append(recursivo(x + 2, y + 1, m8, lista.copy()))

    if len(lista_resposta) == 0:
        a = []
        return(a)
    maior = busca_maior_lista(lista_resposta)
    print(maior)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matriz]))
    print('\n\n')
    return maior


def busca_maior_lista(listas):
    tamanho_lista = -1
    maior_lista = []
    print ('num_listas:' + str(len(listas)))
    for lista in listas:
        if len(lista) > tamanho_lista and len(lista) < 64:
            maior_lista = lista
            tamanho_lista = len(lista)

    return maior_lista


primeirox = 0
primeiroy = 0
#m[primeirox][primeiroy] = 1
#l.append(primeirox * 10 + primeiroy)

try:
    contador = 0
    resultado = recursivo(primeirox, primeiroy, m.copy(), l.copy())
    print('resultado:\n')
    print(resultado)
except Exception as exc:
    traceback.print_exc()
    print(exc)
