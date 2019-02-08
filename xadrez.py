
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
 #se cair fora da lista
 if x < 0 or y < 0 or x > 7 or y > 7:
  return 0
 #se já tenha sido preenchido
 if matriz[x][y] != -1:
  return 0

 # caso passe as verificações, atribuir na matriz
 matriz[x][y] = len(lista)-1
 lista.append(x*10 + y)

 resp1 = recursivo(x-1,y+2,matriz,lista)
 resp2 = recursivo(x-1,y-2,matriz,lista)
 resp3 = recursivo(x+1,y+2,matriz,lista)
 resp4 = recursivo(x+1,y-2,matriz,lista)
 resp5 = recursivo(x-2,y-1,matriz,lista)
 resp6 = recursivo(x+2,y-1,matriz,lista)
 resp7 = recursivo(x-2,y+1,matriz,lista)
 resp8 = recursivo(x+2,y+1,matriz,lista)

 if resp1 != 0:
  return resp1
 if resp2 != 0:
  return resp2
 if resp3 != 0:
  return resp3
 if resp4 != 0:
  return resp4
 if resp5 != 0:
  return resp5
 if resp6 != 0:
  return resp6
 if resp7 != 0:
  return resp7
 if resp8 != 0:
  return resp8

 return 0


primeirox = 0
primeiroy = 0
m[primeirox][primeiroy] = 0
l.append(primeirox * 10 + primeiroy)
resultado = recursivo(primeirox,primeiroy, m,l)
print (resultado)