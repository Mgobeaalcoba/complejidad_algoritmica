import time

def busqueda_lineal(lista, objetivo):
    inicio = time.time()
    match = False

    for element in lista:
        if element == objetivo:
            match = True
            break
    
    fin = time.time()
    duración = fin - inicio
    
    return f'{match}, tardó {duración} segundos.'


def run():


    lista = [x for x in range(1500000)]
    objetivo = 1600000
    objetivo2 = 10000
    objetivo3 = 350000
    objetivo4 = 798000
    objetivo5 = 1499000

    print(f'¿{objetivo} está en la lista?: {busqueda_lineal(lista,objetivo)}')
    print(f'¿{objetivo2} está en la lista?: {busqueda_lineal(lista,objetivo2)}')
    print(f'¿{objetivo3} está en la lista?: {busqueda_lineal(lista,objetivo3)}')
    print(f'¿{objetivo4} está en la lista?: {busqueda_lineal(lista,objetivo4)}')
    print(f'¿{objetivo5} está en la lista?: {busqueda_lineal(lista,objetivo5)}')

    """
    ¿1600000 está en la lista?: False, tardó 0.022828102111816406 segundos.
    ¿10000 está en la lista?: True, tardó 0.0 segundos.
    ¿350000 está en la lista?: True, tardó 0.0040018558502197266 segundos.
    ¿798000 está en la lista?: True, tardó 0.011001110076904297 segundos.
    ¿1499000 está en la lista?: True, tardó 0.011693000793457031 segundos.
    """


if __name__ == '__main__':
    run()

# ¿Cual es la complejidad algoritmica de este algoritmo?: O(n) o lineal