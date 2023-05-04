# Busqueda lineal en una lista desordenada.  

import random

if __name__ == '__main__':
    tamano_de_la_lista = int(input("De que tamaño es la lista? "))
    objetivo = int(input("Que numero quieres encontrar? "))

    lista = [random.randint(0,100) for i in range(tamano_de_la_lista)]

    encontrado = False
    
    print(lista)
    # Usamos un condicional dentro de un string y en una sola linea. Bien pythonico
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
    

# ¿Cual es la complejidad algoritmica de este algoritmo?: O(n) o lineal