import hashlib

def hasheo(mensaje):
    m = hashlib.sha256()
    m.update(mensaje.encode())
    return m.hexdigest()

print(hasheo("Hola"))


def arbol_merkle(a, b, c, d):
    a, b, c, d = hasheo(a), hasheo(b), hasheo(c), hasheo(d)
    nodo_padre1 = hasheo(a + b)
    nodo_padre2 = hasheo(c + d)
    nodo_raiz = hasheo(nodo_padre1 + nodo_padre2)
    print(nodo_raiz)
    return nodo_raiz


arbol_merkle("hola", "Hola", "chao", "Chao")


def arbol_merkle(lista):
    hojas = []
    for i in range (len(lista)):
        hojas.append(hasheo(lista[i]))
    root_hash = construir_arbol_recursivo(hojas)
    print(root_hash)



def construir_arbol_recursivo(hojas):
    if len(hojas) == 1:
        return hojas[0]

    padres = []
    if len(hojas) % 2 == 0:
        for x in range(0, len(hojas), 2):
            padres.append(hasheo(hojas[x] + hojas[x+1]))
        hojas = padres.copy()
        return construir_arbol_recursivo(hojas)

    else:
        hojas.append(hojas[-1])
        for x in range(0, len(lista), 2):
            padres.append(hasheo(hojas[x] + hojas[x+1]))
        hojas = padres.copy()
        return construir_arbol_recursivo(hojas)

    
lista = ["hola", "Hola", "chao", "Chao"]
lista1 = ["Hola"]

arbol_merkle(lista)
arbol_merkle(lista1)

        






