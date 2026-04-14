import timeit
import random
import sys

'''Cambiamos el limite de recursion. Cuando insertamos los datos ordenados
y empezamos a hacer llamadas recursivas para la busqueda, python arroja un error para evitar el 
desbordamiento de memoria. Para poder testear lo que sucede cuando insertamos ordenados, cambio el limite.'''
sys.setrecursionlimit(20000)

# Importamos tus clases desde los otros archivos
from ArbolABB import ArbolABB
from arbolBplus import ArbolBPlus

# --- CONFIGURACIÓN ---
CANTIDAD = 10000  #Numero de estudiantes_ordenados a registrar
BUSQUEDAS_ID = 100 #IDS que vamos a buscar para medir los tiempos. Los vamos aumentando para notar el cambio en busquedas grandes vs busquedas pequenas
ORDEN_BPLUS = 10 #Numero de claves posibles por nodo interno (no hoja)
REPETICIONES = 10 #Numero de veces a repetir la ejecucion para promediar y reducir factores de ruido relacionados a IDE, CPU, etc.

# 1. GENERACIÓN DE DATOS
estudiantes_ordenados = [] #Arreglo de los estudiantes_ordenados ORDENADOS a registrar
for i in range(CANTIDAD): #repetir CANTIDAD veces (numero estudiantes_ordenados)
    estudiantes_ordenados.append({
        "id": 1000 + i, #ids asociados secuencialmente
        "nombre": f"Estudiante_{i}", #Nombre generico
        "promedio": round(random.uniform(6.0, 10.0), 1)  #estudiantes_ordenados registrados, con ids desde el 1000 hasta el 11000. 
    })

# IDs para buscar (aleatorios para que sea una prueba real)
ids_a_buscar = [random.randint(1000, 1000 + CANTIDAD - 1) for _ in range(BUSQUEDAS_ID)]  #Escoge numeros del 1000 al 10000 aleatoriamente para realizar las busquedas
estudiantes_Random = estudiantes_ordenados.copy()
random.shuffle(estudiantes_Random)

def ejecutar_pruebas(lista_datos, titulo): #Pasamos como parametro la lista de los estudiantes, y el titulo, ejemplo ordenado o desordenado
    print(f"\n{'='*15} {titulo} {'='*15}")
    print(f"Promediando resultados sobre {REPETICIONES} ejecuciones, para {BUSQUEDAS_ID} busquedas ...")
    
    # Inicializar estructuras  #Se inician los arboles y se llenan con base a la lista que le pasamos (sea ordenada o desordenada)
    abb = ArbolABB()
    bplus = ArbolBPlus(orden=ORDEN_BPLUS)
    
    # Llenar árboles
    for i in range(len(lista_datos)):
        abb.insertar(lista_datos[i]["id"], i)
        bplus.insertar(lista_datos[i]["id"], i)

    '''Se realizan las 3 pruebas correspondientes
    Busqueda lineal en una lista
    Busqueda en el arbol abb
    Busqueda en el arbol b+
    Por ultimo hace una comparacion entre los dos arboles e imprime todo'''
    def test_lista():
        for target in ids_a_buscar:
            for est in lista_datos:
                if est["id"] == target: break

    def test_abb():
        for target in ids_a_buscar:
            abb.buscar(target)

    def test_bplus():
        for target in ids_a_buscar:
            bplus.buscar(target)

    t_lista = timeit.timeit(test_lista, number=REPETICIONES) / REPETICIONES #Ejecuta cada funcion de busqueda REPETICIONES veces y las promedia. Esto para reducir ruido.
    t_abb   = timeit.timeit(test_abb,   number=REPETICIONES) / REPETICIONES
    t_bplus = timeit.timeit(test_bplus, number=REPETICIONES) / REPETICIONES
    
    print(f"Lista Secuencial: {t_lista:.6f} seg")
    print(f"Árbol ABB:        {t_abb:.6f} seg")
    print(f"Árbol B+:         {t_bplus:.6f} seg")
    print("-" * 30)
    
    #COMPARACION ENTRE TIEMPOS
    if t_bplus > 0:
        proporcion = t_abb / t_bplus
        if proporcion > 1:
            print(f"ANÁLISIS: El Árbol B+ es {proporcion:.2f}x más rápido que el ABB.")
        else:
            # En caso muy raro de que el ABB sea más rápido (solo con muy pocos datos)
            print(f"ANÁLISIS: El ABB es {1/proporcion:.2f}x más rápido que el B+.")
    
    # Comparación con la lista para ver el poder del indexamiento
    proporcion_lista = t_lista / (t_bplus if t_bplus > 0 else 0.000001)
    print(f"ANÁLISIS: El Árbol B+ es {proporcion_lista:.2f}x más rápido que la búsqueda lineal.")
    print("-" * 30)
    
    # Imprimir resultados del bloque
    
    
# --- EJECUCIÓN DEL EXPERIMENTO ---

# Prueba A: Datos Ordenados (El ABB se vuelve una lista)
ejecutar_pruebas(estudiantes_ordenados, "ESCENARIO A: DATOS ORDENADOS")

# Prueba B: Datos Aleatorios (El ABB se balancea naturalmente)
ejecutar_pruebas(estudiantes_Random, "ESCENARIO B: DATOS ALEATORIOS")
