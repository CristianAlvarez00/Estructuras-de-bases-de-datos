import hashlib
import arbolMerklePromoviendo
import random

def hashInverso(hash):
    for i in range(10000000000): #Numero maximo que puede tener la secuencia (9999999999)
        
        candidato = str(i).zfill(10) #Se escogen enteros desde 0 hasta 9999999999 y se rellena el resto con 0s
        hash_candidato = hashlib.sha256(candidato.encode()).hexdigest() #Hashea el numero i completado con los 0s correspondientes
        if hash_candidato == hash: #Si ese numero i, al hashearse, corresponde al hash que nosotros estabamos buscando:
            print("La secuencia de numeros que genera el hash " + hash + " es " + candidato) # Se imprime la secuencia encontrada
            return candidato #Retornamos el candidato una vez hallado
    
    print("No se encontro la secuencia de numeros.") #Si despues de ejecutado con todas las secuencias hasta 9999999999, no se encontro, imprimimos dicho resultado.




def encontrarOrdenTransacciones(hash_root, transacciones): #Ingresamos como parametro el hashroot y las transacciones en un orden n
    # Hacemos una copia inicial para no destruir la original
    lista_para_shuffle = transacciones.copy()
    
    # Calculamos el primer candidato
    candidato = arbolMerklePromoviendo.arbol_merkle(lista_para_shuffle.copy())

    while hash_root != candidato:
        random.shuffle(lista_para_shuffle) #Revolvemos la lista
        # IMPORTANTE: Pasamos una COPIA a la función para que no la vacíe
        candidato = arbolMerklePromoviendo.arbol_merkle(lista_para_shuffle.copy()) #Construimos el arbol con las transacciones revueltas
                                                                        #Hasta que su hashroot coincida con el del parametro. Cuando coincida, sale del loop.
    
    print("El orden de las transacciones es: ")
    for i, tx in enumerate(lista_para_shuffle):
        flecha = "└── " if i == len(lista_para_shuffle) - 1 else "├── "
        print(f"{flecha}Posición {i}: {tx}")

def menu():
    while True:
        print("\n--- MENÚ DE PRUEBAS - ÁRBOL MERKLE Y HASH ---")
        print("1. Encontrar secuencia de números (Hash Inverso)")
        print("2. Encontrar orden de transacciones (Merkle Root)")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            h = input("Ingrese el hash SHA-256 a descifrar: ")
            print("Buscando secuencia (esto puede tardar)...")
            hashInverso(h)

        elif opcion == "2":
            root_objetivo = input("Ingrese el Merkle Root objetivo: ")
            datos = input("Ingrese las transacciones separadas por coma: ")
            lista_txs = [t.strip() for t in datos.split(",")]
            
            print("Buscando el orden correcto...")
            encontrarOrdenTransacciones(root_objetivo, lista_txs)

        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

