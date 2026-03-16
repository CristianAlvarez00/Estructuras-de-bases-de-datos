import random
import time
import random
import sys
'''Cambiamos el limite de recursion. Cuando insertamos los datos ordenados
y empezamos a hacer llamadas recursivas para la busqueda, python arroja un error para evitar el 
desbordamiento de memoria. Para poder testear lo que sucede cuando insertamos ordenados, cambio el limite.'''


class NodoABB: 
    def __init__(self, id, indice): #Creamos el nodo insertando el id del registro, y el indice donde se halla el registro completo
        self.id = id 
        self.indice = indice
        self.izq = None #hijos izq y derecho, por defecto en None
        self.der = None
class ArbolABB:
    def __init__(self):
        self.raiz = None # Raiz del arbol
    def insertar(self, id, indice): #Para insertar una clave, pasamos el id o la clave junto con el indice del registro
        if self.raiz is None: 
            self.raiz = NodoABB(id, indice) #Si no hay ningun nodo en el arbol (arbol vacio), hacemos que el nodo insertado sea la raiz
        else:
            self._insertar(self.raiz, id, indice) #Si no, ejecutamos la funcion _insertar (tiene mas parametros, se divide asi para que sea mas amigable al usarla)

    def _insertar(self, nodo, id, indice): #nodo, en principio, es el nodo raiz porque empezamos a descender desde ese.
                                           #los demas paarametros son los mismos necesarios, la clave y el indice del registro
        if id == nodo.id: #si detectamos que la clave YA ESTA, quebramos la funcion.
            return
        elif id < nodo.id: #Si el id del nodo a insertar es menor que el del nodo en que estamos parados:
            if nodo.izq is None: # Si llegamos a un espacio disponible:
                nodo.izq = NodoABB(id, indice) #Insertamos el nodo en esa posicion
            else:
                self._insertar(nodo.izq, id, indice) #Si no esta disponible el espacio, seguimos descendiendo

        elif id > nodo.id: #Si el id del nodo a insertar es mayor que el del nodo en que estamos parados:
            if nodo.der is None: #si el espacio esta disponibleL:
                nodo.der = NodoABB(id, indice) #insertamos en esa posicion el nodo
            else:
                self._insertar(nodo.der, id, indice) #Si no esta disponible, seguimos descendiendo.
    def buscar(self, id): #ingresamos la clave a buscar
        return self._buscar(self.raiz, id) #Usamos otra funcion (mas amigable para el user)

    def _buscar(self, nodo, id): #Pasamos como parametro el nodo en que estamos parados (empezando por la raiz) y la clave.

        if nodo is None: #Si no hay nodo raiz, o desciende a un nodo vacio, quiebra la funcion (no esta la clave en el arbol)
            return None

        if id == nodo.id: #Si en el nodo en que estamos parados encontramos la clave, retornamos el indice para el registro COMPLETO
            return nodo.indice

        elif id < nodo.id: #Si el id a buscar es menor que el id del nodo en que estamos, descendemos a la izquierda
            return self._buscar(nodo.izq, id)

        else: #Si el id a buscar es mayor que el id del nodo en que estamos, descendemos a la derecha.
            return self._buscar(nodo.der, id)
    
    def listar_en_orden(self, lista): #Ordenar los registros del arbol con la clave. Retornamos el arreglo con las claves ordenadas
        resultado = [] #inicializamos lista vacia
        self._inorden(self.raiz, resultado, lista)
        return resultado 

    def _inorden(self, nodo, resultado, lista): #Pasamos como parametro el nodo raiz, y vamos descendiendo de nodo

        if nodo is not None:
            self._inorden(nodo.izq, resultado, lista) #Metemos primero el nodo hijo a la izquierda
            resultado.append(lista[nodo.indice]) #Despues incluimos el nodo padre (valor medio)
            self._inorden(nodo.der, resultado, lista) #por ultimo metemos el nodo hijo derecho, el mayor.

    





