# Conteo abstracto de operacion:

# Determinación de la cantidad de operaciones que va a realizar
# un algoritmo:

def f(x):

    respuesta = 0 # 1 operacion

    for i in range(1000): # 1000 operaciones
        respuesta += 1

    for i in range(x): # X operaciones
        respuesta += 1

    for i in range(x): 
        for j in range(x): # X * X por 2 operaciones = 2X**2
            respuesta += 1
            respuesta += 1

    return respuesta # 1 operaciones

# ¿Cuantas operaciones va a hacer nuestra funcion entonces? 

# 1 + 1000 + X + 2x**2 + 1

if __name__ == '__main__':
    print(f(50)) # 6050 operaciones
    print(f(123)) # 31381 operaciones