import hashlib

def hasheo(mensaje):
    return hashlib.sha256(mensaje.encode()).hexdigest() ##Funcion para hashear mensaje o transaccion.

def construir_arbol_recursivo(hojas):
    # Caso base: solo queda un hash, es la raíz
    if len(hojas) == 1:
        return hojas[0] #Caso base, retorna el hash root

    padres = [] 
    # Recorremos de 2 en 2
    for i in range(0, len(hojas) - 1, 2):
        padres.append(hasheo(hojas[i] + hojas[i+1])) #añadimos en la lista de dos en dos

    # METODOLOGÍA DE ASCENSO (PROMOCIÓN):
    # Si el número de hojas es impar, el último elemento no entró en el loop.
    # Lo subimos directamente al siguiente nivel.
    if len(hojas) % 2 != 0: 
        padres.append(hojas[-1])

    return construir_arbol_recursivo(padres)

def arbol_merkle(lista): ##Construccion del arbol
    if not lista:
        return None
    hojas = [hasheo(item) for item in lista]
    root_hash = construir_arbol_recursivo(hojas)
    print(f"Lista: {lista} -> Root: {root_hash}")
    return root_hash

