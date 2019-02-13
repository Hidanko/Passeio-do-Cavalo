import traceback

m = [[-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1]]
l = []


# caso retorne 0 = sem saída
def recursivo(x, y, matriz, lista):
    if len(lista) == 33:
        print('a')

    if len(lista) == 64:
        return lista.copy()

    # caso passe as verificações, atribuir na matriz
    lista.append(x * 10 + y)
    matriz[x][y] = len(lista)

    lista_resposta = []
    lista_len = len(lista)
    if x - 1 >= 0 and y + 2 <= 7:
        if matriz[x - 1][y + 2] == -1:
            m1 = matriz.copy()
            m1[x - 1][y + 2] = lista_len
            lista_resposta.append(recursivo(x - 1, y + 2, m1, lista.copy()))
    if x - 1 >= 0 and y - 2 >= 0:
        if matriz[x - 1][y - 2] == -1:
            m2 = matriz.copy()
            m2[x - 1][y - 2] = lista_len
            lista_resposta.append(recursivo(x - 1, y - 2, m2, lista.copy()))
    if x + 1 <= 7 and y + 2 <= 7:
        if matriz[x + 1][y + 2] == -1:
            m3 = matriz.copy()
            m3[x + 1][y + 2] = lista_len
            lista_resposta.append(recursivo(x + 1, y + 2, m3, lista.copy()))
    if x + 1 <= 7 and y - 2 >= 0:
        if matriz[x + 1][y - 2] == -1:
            m4 = matriz.copy()
            m4[x + 1][y - 2] = lista_len
            lista_resposta.append(recursivo(x + 1, y - 2, m4, lista.copy()))
    if x - 2 >= 0 and y - 1 >= 0:
        if matriz[x - 2][y - 1] == -1:
            m5 = matriz.copy()
            m5[x - 2][y - 1] = lista_len
            lista_resposta.append(recursivo(x - 2, y - 1, m5, lista.copy()))
    if x + 2 <= 7 and y - 1 >= 0:
        if matriz[x + 2][y - 1] == -1:
            m6 = matriz.copy()
            m6[x + 2][y - 1] = lista_len
            lista_resposta.append(recursivo(x + 2, y - 1, m6, lista.copy()))
    if x - 2 >= 0 and y + 1 <= 7:
        if matriz[x - 2][y + 1] == -1:
            m7 = matriz.copy()
            m7[x - 2][y + 1] = lista_len
            lista_resposta.append(recursivo(x - 2, y + 1, m7, lista.copy()))
    if x + 2 <= 7 and y + 1 <= 7:
        if matriz[x + 2][y + 1] == -1:
            m8 = matriz.copy()
            m8[x + 2][y + 1] = lista_len
            lista_resposta.append(recursivo(x + 2, y + 1, m8, lista.copy()))

    maior = longest(lista_resposta)
    print(maior)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matriz]))
    print('\n\n')
    return maior


def longest(listas):
    tamanho_lista = -1
    maior_lista = []
    print ('num_listas:' + str(len(listas)))
    for lista in listas:
        if len(lista) > tamanho_lista and len(lista) < 64:
            maior_lista = lista
            tamanho_lista = len(lista)

    return maior_lista


primeirox = 5
primeiroy = 5
m[primeirox][primeiroy] = 0
# l.append(primeirox * 10 + primeiroy)
try:
    resultado = recursivo(primeirox, primeiroy, m, l)
    print('resultado:\n')
    print(resultado)
except Exception as exc:
    traceback.print_exc()
    print(exc)
