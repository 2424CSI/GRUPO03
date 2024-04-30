import numpy as np  

# Solicitar al usuario que ingrese el número de columnas y el mensaje
n = int(input("Ingrese el número de columnas: "))
while n <= 0:
    n = int(input("Ingrese el número válido: "))
    
mensaje = input("Ingrese el mensaje: ")
while (mensaje == ""):
        mensaje = input("Ingresa una palabra: ")

# Eliminar los espacios del mensaje
mensaje = mensaje.replace(" ", "")  

# Comprobar si el número de caracteres del mensaje es menor o igual a n x n
if len(mensaje) > n*n:
    print("El mensaje es demasiado largo para la clave proporcionada.")
else:
    # Crear una matriz de cifrado de tamaño n x n
    matriz = np.full((n, n), "*")

    # Llenar la matriz con el mensaje, columna por columna
    for j in range(n):
        for i in range(n):
            if j*n + i < len(mensaje):
                matriz[i, j] = mensaje[j*n + i]

    # Imprimir la matriz de cifrado, el mensaje original y el mensaje cifrado
    print("Matriz de cifrado:")
    print(matriz)
    print("Mensaje original:", mensaje)
    print("Mensaje cifrado:", "".join(matriz.flatten()))