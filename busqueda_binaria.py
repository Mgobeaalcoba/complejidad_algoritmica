# Busqueda binaria o "divide y conquista". Va a reducir el universo siempre a la mitad
# Trade off: Tiempo y Memoría. 

import random

# Algoritmo de busqueda binaria recursivo: 
def busqueda_binaria(lista, comienzo, final, objetivo):

    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == '__main__':
    tamano_de_la_lista = int(input("De que tamaño es la lista? "))
    objetivo = int(input("Que numero quieres encontrar? "))

    # sorted ordena de forma ascendente por default.
    lista = sorted([random.randint(0,100) for i in range(tamano_de_la_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    
    print(lista)
    # Usamos un condicional dentro de un string y en una sola linea. Bien pythonico
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
