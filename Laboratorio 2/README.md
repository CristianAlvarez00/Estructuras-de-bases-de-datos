# Laboratorio 2: Árboles de Merkle y Criptografía

Este repositorio contiene la implementación de un Árbol de Merkle utilizando la metodología de **promoción de nodos** para manejar listas de transacciones impares. También incluye herramientas para búsqueda de colisiones de hash por fuerza bruta.

## Contenido del Proyecto
* `arbolMerklePromoviendo.py`: Lógica del árbol con ascenso de nodos huérfanos.
* `main.py`: Interfaz de usuario con menú para pruebas de hash inverso y ordenamiento.

## Funcionalidades principales
1. **Construcción de Merkle Root**: Cálculo recursivo de la raíz del árbol.
2. **Hash Inverso**: Búsqueda de secuencias numéricas a partir de un hash SHA-256.
3. **Reordenamiento de Transacciones**: Algoritmo de búsqueda aleatoria para encontrar el orden original que generó un Merkle Root específico.

## Cómo ejecutar
1. Clonar el repositorio.
2. Ejecutar `python main.py`.
3. Seguir las instrucciones del menú en consola.