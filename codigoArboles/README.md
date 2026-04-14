El objetivo central es analizar cómo la organización interna de los nodos y el orden de inserción de los datos afectan el tiempo de respuesta a la hora de realizar búsquedas de información, en diferentes estructuras: Árboles ABB y B+, y búsqueda lineal en una lista.

# Instrucciones
1. Clonar este repositorio o descargar los 3 archivos en una misma carpeta.
2. Abrir una terminal o consola en dicha carpeta.
3. Ejecutar el script principal python main.py. Puede modificar las constantes para evaluar el rendimiento del programa, tales como:
*cantidad de registros a generar 
*cantidad de ids a buscar
*cantidad de veces a repetir para promediar
*el limite de claves-referencias por nodo en el arbol b+

Metodología y estadística

Para obtener resultados válidos, se implementó un sistema de **muestreo y promediado** para mitigar factores externos:

1. **Reducción de Ruido:** Queremos que el sesgo asociado a los procesos en segundo plano, o picos en el uso del CPU, se reduzca a la hora de evaluar el rendimiento de los algoritmos.
2. **Promedio de Ejecuciones:** Cada prueba de búsqueda se repite `REPETICIONES` veces. Se utiliza la librería `timeit` para obtener el tiempo acumulado y luego calcular la media aritmética.
3. **Escenarios Comparativos:**
   * **Escenario A (Datos Ordenados):** Evalúa el comportamiento de las estructuras ante entradas secuenciales, exponiendo la vulnerabilidad del ABB a la degeneración (árbol desbalanceado).
   * **Escenario B (Datos Aleatorios):** Evalúa el rendimiento en condiciones óptimas de distribución para estructuras de árbol.

## 1. Componentes del Sistema

* `ArbolABB.py`: Implementación de un árbol binario estándar con inserción y búsqueda recursiva.
* `arbolBplus.py`: Implementación de un Árbol B+ balanceado. Maneja nodos internos y hojas ligadas, garantizando una altura $O(\log n)$.
* `main.py`: Script principal que orquesta el experimento, genera los objetos de datos y calcula las métricas finales.

### 2. Configuración de Parámetros 
Dentro de `main.py`, se pueden ajustar las constantes globales para profundizar en el análisis estadístico:
* `CANTIDAD`: Total de registros a insertar (ej. 10,000).
* `BUSQUEDAS_ID`: Cantidad de claves diferentes a buscar en cada iteración.
* `REPETICIONES`: Factor de repetición para el cálculo del promedio (limpia el ruido del sistema).
* `ORDEN_BPLUS`: Grado del Árbol B+ (máximo de llaves/hijos por nodo).

### 3. Ejecución

Una vez seteadas las constantes (ya llevan una configuracion por defecto), solo se debe correr ***main.py***.