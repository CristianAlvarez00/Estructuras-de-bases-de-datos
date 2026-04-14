import math
import time
import random

class NodoBPlus:
    def __init__(self, hoja=False): #Para crear un nodo, debemos definir si es un nodo interno o si es una hoja.
        self.hoja = hoja
        self.llaves = []
        self.indices = []  # Solo para hojas, ya que las hojas son las que incluyen los datos reales
        self.hijos = []    # Solo para nodos internos 
        self.sig = None    # Puntero a la siguiente hoja (lista ligada)

class ArbolBPlus: 
    def __init__(self, orden=4): #Ingresamos el numero de claves admitidas por nodo
        self.raiz = NodoBPlus(True) #En principio la raiz es una hoja
        self.orden = orden

    def buscar(self, k): #Parametro, la clave a buscar.
        n = self.raiz
        while not n.hoja: #Mientras NO sea una hoja: Es decir, bajaremos hasta que nos hallemmos en una hoja

            i = 0 #Indicador de la posicion en el nodo donde encontramos la clave.

            #SI i es mayor= que el numero de hijos O la llave a buscar es menor que la llave en que estamos parados, salimos del while
            while i < len(n.llaves) and k >= n.llaves[i]: #esta instruccion lo que hace es, ubicarnos una posicion ANTES de la clave del hijo mas grande que encontremos.
                                                          #si no encontramos una mas grande, significa que va en la ultima posicion. 
                
                i += 1
            n = n.hijos[i] #Una vez determinada la posicion en la que vamos, nos paramos en ella. 
        
        for i in range(len(n.llaves)): #Estando parado en n (seria el nodo justo antes de la hoja que contiene la clave)
            if n.llaves[i] == k: #Comparamos con todos los valores que hay en esa hoja hasta encontrarla
                return n.indices[i]
        return None

    def insertar(self, k, idx): #Para insertar, ingresamos la clave y el indice de la clave para encontrar el registro.
        hoja = self._buscar_hoja(k) #Con esta funcion hallamos en qué parte del arbol, en que hoja, va la clave k.
        self._insertar_en_hoja(hoja, k, idx) #Funcion mas especifica para insertar en la hoja encontrada, la clave y el indice dados.
        if len(hoja.llaves) >= self.orden: #Si la cantidad de claves en la hoja es mayor que el orden que escogimos, se DIVIDE la hoja
            self._split_hoja(hoja) 

    def _buscar_hoja(self, k): #Buscamos en qué hoja del árbol debe ir el dato k
        n = self.raiz #Empezamos descendiendo desde la raiz
        while not n.hoja: #mientras que no estemos parados en una hoja
            i = 0
            while i < len(n.llaves) and k >= n.llaves[i]: #Volvemos a comparar con cada referencia del nodo hasta ubicar en qué parte va
                i += 1
            n = n.hijos[i] #guardamos la posicion en donde deberia ir la k (coincide con la posicion en donde deberiamos encontrarla si estuviese)
        return n

    def _insertar_en_hoja(self, hoja, k, idx): #Habiendo encontrado la hoja donde va, procedemos:
        i = 0
        while i < len(hoja.llaves) and k > hoja.llaves[i]: #Bajo la misma logica, volvemos a encontrar en qué parte de la hoja va la clave (igual que cuando intentabamos encontrar en que parte del nodo va la referencia)
            i += 1 #Con este contador encontramos la posicion donde debe ir la clave.
        hoja.llaves.insert(i, k) #en el conjunto de las llaves de la hoja, insertamos la nueva llave en la posicion i que encontramos
        hoja.indices.insert(i, idx) #En el conjunto de indices (que estan asociados a las llaves), insertamos el indice de la clave k.

    def _split_hoja(self, hoja): #En caso de que la hoja haya alcanzado el limite de datos en la hoja:
        nueva = NodoBPlus(True) #Creamos un nuevo nodo
        mid = len(hoja.llaves) // 2 #Mitad del numero de datos que hay en el nodo
        
        nueva.llaves = hoja.llaves[mid:] #Tomamos desde la mitad hacia adelante de las claves.
        nueva.indices = hoja.indices[mid:] #Tomamos desde la mitad hacia adelante de los indices de los registros.
        hoja.llaves = hoja.llaves[:mid] #Ahora, las claves del nodo en que estamos parados las tomamos hasta la mitad
        hoja.indices = hoja.indices[:mid] #Tomamos los indices de las claves hasta la mitad. 
        
        nueva.sig = hoja.sig #Conectamos, de la hoja llena, el nodo que le sigue con la nueva division derecha que generamos.
        hoja.sig = nueva #Ahora, conectamos la division derecha del nodo lleno con la division derecha del mismo.
        
        self._subir_llave(hoja, nueva.llaves[0], nueva) #Funcion para subir llave, escogiendo como referencia el valor "medio" k que divide a las dos hojas nuevas izq y der

    def _subir_llave(self, izq, k, der):
        padre = self._encontrar_padre(self.raiz, izq) #Encontramos cual es el nodo padre del hijo que teniamos antes (parte izquierda)
        
        if padre is None: #si no hay padre significa que llegamos a la raiz
            nueva_raiz = NodoBPlus(False)
            nueva_raiz.llaves = [k]
            nueva_raiz.hijos = [izq, der]
            self.raiz = nueva_raiz
            return

        i = 0
        while i < len(padre.llaves) and k > padre.llaves[i]: #Si hay padre, entonces hallamos en que posicion debe ir la llave
            i += 1
        padre.llaves.insert(i, k) #Una vez encontrada la posicion i de la llave, insertamos la llave.
        padre.hijos.insert(i + 1, der) #insertamos el nuevo hijo, que es la division derecha

        if len(padre.llaves) >= self.orden: #Si la longitud del padre tambien alcanzo el limite, hay que dividir tambien el padre
            self._split_interno(padre)

    def _split_interno(self, nodo): #seguimos el mismo proceso que en el anterior
        nueva = NodoBPlus(False)
        mid = len(nodo.llaves) // 2
        llave_subir = nodo.llaves[mid]
        
        nueva.llaves = nodo.llaves[mid + 1:]
        nueva.hijos = nodo.hijos[mid + 1:]
        nodo.llaves = nodo.llaves[:mid]
        nodo.hijos = nodo.hijos[:mid + 1]
        
        self._subir_llave(nodo, llave_subir, nueva)

    def _encontrar_padre(self, actual, objetivo): #Con este, buscamos el padre del nodo (objetivo), parandonos en cada nodo (actual)
        if actual.hoja or objetivo == self.raiz: #Si llegamos a una hoja, no se encontro padre del objetivo, y si el padre es la raiz, retornamos none
            return None
        for hijo in actual.hijos: 
            if hijo == objetivo: #Si encontramos la referencia en un nodo en el conjunto de hijos del nodo, ya tenemos al padre.
                return actual 
            res = self._encontrar_padre(hijo, objetivo)# Si no es mi hijo, le pido a este hijo que busque en su propia familia.
            if res: 
                return res #Si encontramos en uno de los hijos de los hijos, al objetivo, lo retonarmos. Si no, no se encontro el padre.
        return None