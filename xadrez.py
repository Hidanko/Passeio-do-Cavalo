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
    if len(lista) == 64:
        return lista

    # caso passe as verificações, atribuir na matriz
    matriz[x][y] = len(lista) - 1
    lista.append(x * 10 + y)
    if x - 1 >= 0 and y + 2 <= 7:
        if matriz[x - 1][y + 2] == -1:
            matriz[x - 1][y + 2] = len(lista)
            resp1 = recursivo(x - 1, y + 2, matriz, lista)
            if resp1 != 0:
                return resp1
    if x - 1 >= 0 and y - 2 >= 0:
        if matriz[x - 1][y - 2] == -1:
            matriz[x - 1][y - 2] = len(lista)
            resp2 = recursivo(x - 1, y - 2, matriz, lista)
            if resp2 != 0:
                return resp2
    if x + 1 <= 7 and y + 2 <= 7:
        if matriz[x + 1][y + 2] == -1:
            matriz[x + 1][y + 2] = len(lista)
            resp3 = recursivo(x + 1, y + 2, matriz, lista)
            if resp3 != 0:
                return resp3
    if x + 1 <= 7 and y - 2 >= 0:
        if matriz[x + 1][y - 2] == -1:
            matriz[x + 1][y - 2] = len(lista)
            resp4 = recursivo(x + 1, y - 2, matriz, lista)
            if resp4 != 0:
                return resp4
    if x - 2 >= 0 and y - 1 >= 0:
        if matriz[x - 2][y - 2] == -1:
            matriz[x - 2][y - 2] = len(lista)
            resp5 = recursivo(x - 2, y - 1, matriz, lista)
            if resp5 != 0:
                return resp5
    if x + 2 <= 7 and y - 1 >= 0:
        if matriz[x + 2][y - 1] == -1:
            matriz[x + 2][y - 1] = len(lista)
            resp6 = recursivo(x + 2, y - 1, matriz, lista)
            if resp6 != 0:
                return resp6
    if x - 2 >= 0 and y + 1 <= 7:
        if matriz[x - 2][y + 1] == -1:
            matriz[x - 2][y + 1] = len(lista)
            resp7 = recursivo(x - 2, y + 1, matriz, lista)
            if resp7 != 0:
                return resp7
    if x + 2 <= 7 and y + 1 <= 7:
        if matriz[x + 2][y + 1] == -1:
            matriz[x + 2][y + 1] = len(lista)
            resp8 = recursivo(x + 2, y + 1, matriz, lista)
            if resp8 != 0:
                return resp8

    return lista


primeirox = 0
primeiroy = 0
m[primeirox][primeiroy] = 0
l.append(primeirox * 10 + primeiroy)
try:
    resultado = recursivo(primeirox, primeiroy, m, l)
    print(resultado)
except Exception as exc:
    print(exc)