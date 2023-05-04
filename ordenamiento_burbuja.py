# Ordenamiento que compara elementos adyacentes y los intercambia
# si están en el orden incorrecto. Este procedimiento se repite
# hasta que ya no se requieren mas intercambios. Lo que indica que 
# la lista está completamente ordenada. 

# Si solo quisieramos encontrar el elemento mas grande, o el mas
# pequeño, podríamos hacerlo en un solo paso. Esto significa O(n)
# o un algoritmo de complejidad lineal. 

import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                # Swiming o intercambio en una linea:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

if __name__ == '__main__':
    tamaño_de_la_lista = int(input("De que tamaño será la lista? "))

    lista = [random.randint(0,100) for i in range(tamaño_de_la_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

    # Complejidad O(n**2) o complejidad cuadratico o polinominial
    # Al ser polinominial nos va a servir con listas chicas, 1000 elementos como mucho
    # Pero si ponemos una lista de 1000000 de elementos rompemos todo. 
    # Para estos casos debemos recurrir a otras estrategias de ordenación.
    

