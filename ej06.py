def generar_matriz_cifrado():
    matriz = [
        ['*', 'A', 'S', 'D', 'F', 'G'],
        ['Q', 'a', 'b', 'c', 'd', 'e'],
        ['W', 'f', 'g', 'h', 'i', 'j'],
        ['E', 'k', 'l', 'm', 'n', 'o'],
        ['R', 'p', 'q', 'r', 's', 't'],
        ['T', 'u', 'v', 'x', 'y', 'z']
    ]
    return matriz

def cifrar_mensaje(matriz, mensaje):
    mensaje_cifrado = ""
    for letra in mensaje:
        cifrada = False
        for i, fila in enumerate(matriz):
            for j, caract in enumerate(fila):
                
                if caract == letra:
                    mensaje_cifrado += f"{fila[0]}{matriz[0][j]}"
                    cifrada = True
                    break
            if cifrada:
                break
        if not cifrada:
            mensaje_cifrado += "**"
    return mensaje_cifrado

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))

# Función principal
def main():
    matriz_cifrado = generar_matriz_cifrado()
    
    mensaje_original = input("Ingresa el mensaje a cifrar: ").lower()
    
    while mensaje_original=="":
         mensaje_original = input("Ingrese una palabra: ").lower()
        
    print("\nMatriz de cifrado:")
    imprimir_matriz(matriz_cifrado)

    mensaje_cifrado = cifrar_mensaje(matriz_cifrado, mensaje_original)

    print("\nMensaje original:", mensaje_original)
    print("Mensaje cifrado:", mensaje_cifrado)

# Llamar a la función principal
if __name__ == "__main__":
    main()
