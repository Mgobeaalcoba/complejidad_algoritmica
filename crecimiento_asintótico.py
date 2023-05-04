## Crecimiento asintótico

# No importan las variaciones pequeñas de nuestros algoritmos
# El enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito
# Mejor de los casos, promedio, peor de los casos
# Big O Notation
# Nada mas importa el termino de mayor tamaño, no todo el algoritmo (ver segundo ejemplo)

# Ejemplo: 

# Ley de la suma:

def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n)

# Esta función crece de forma lineal. Esto es lo que importa. 

# Esta funcion crece en "O de N" o en "Big O of N" -> Esta es la forma de decirlo.

# Otra ejemplo de ley de suma: 

def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

# O(n) + O(n * n) = O(n + n**2) = O(n**2)

# Esta funcion crece en "O de N al Cuadrado" o en "Big O of N al Cuadrado" -> Esta es la forma de decirlo.

# Estamos frente a una función cuadratica. 

# Ley de la multiplicación: 

def f(n):
    for i in range(n):

        for j in range(n * n):
            print(i, j)

# O(n) * O(n) = O(n + n) = O(n**2)

# Estamos frente a otra función cuadratica.

# Cuando vemos loops dentro de loops estamos, probablemente, frente a funciones de crecimiento cuadratico

# Recursividad múltiple: 

def fibonacci(n):

    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

# O(2**n) Llamamos a la función 2 veces por cada vez de n.


