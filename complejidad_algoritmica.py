import time
import sys

# Factorial sin recursividad
def factorial(n: int):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

# Factorial con recursividad:

def factorial_r(n: int):
    if n == 1:
        return 1
    
    return n * factorial_r(n-1)

def run():
    # print(sys.getrecursionlimit())
    n: int = 100000
    numero_limite = n+100
    sys.setrecursionlimit(numero_limite)
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f'Duración del algoritmo NO recursivo para {n}: {final - comienzo}')
    # Duración del algoritmo NO recursivo 0.0
    # Duración del algoritmo NO recursivo 0.01562356948852539
    # Para 20000: Duración del algoritmo NO recursivo para 20000: 0.09467506408691406
    # Para 5000: Duración del algoritmo NO recursivo para 5000: 0.00225067138671875
    # Para 100000: Duración del algoritmo NO recursivo para 100000: 5.318419933319092
    comienzo2 = time.time()
    factorial_r(n)
    final2 = time.time()
    print(f'Duración del algoritmo recursivo para {n}: {final2 - comienzo2}')
    # RecursionError: maximum recursion depth exceeded (995 recursiones)
    # Duración del algoritmo recursivo 0.0
    # Para 20000: Duración del algoritmo recursivo para 20000: 0.11538076400756836
    # Para 5000: Duración del algoritmo recursivo para 5000: 0.006018400192260742
    # Para 100000: Duración del algoritmo recursivo para 100000: 4.59206223487854

# En algunos casos la recursividad tarda mas que la no recursividad y viceversa.
# No es posible prever la perfo de ambas alternativas antes de ponerlas en practica

if __name__ == '__main__':
    run()