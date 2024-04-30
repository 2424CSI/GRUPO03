import string

def cifrado_monoalfabetico_desplazamiento(cadena, n):
    # Crear alfabeto original
    alfabeto_original = string.ascii_lowercase

    # Crear alfabeto cifrado desplazado n caracteres a la derecha
    alfabeto_cifrado = alfabeto_original[n:] + alfabeto_original[:n]

    # Cifrar la cadena de caracteres
    resultado_cifrado = ""
    for char in cadena:
        if char.lower() in alfabeto_original:
            idx = alfabeto_original.index(char.lower())
            if char.islower():
                resultado_cifrado += alfabeto_cifrado[idx]
            else:
                resultado_cifrado += alfabeto_cifrado[idx].upper()
        else:
            resultado_cifrado += char

    # Mostrar el resultado
    print("Alfabeto original:", alfabeto_original)
    print("Alfabeto cifrado:", alfabeto_cifrado)
    print("Cadena de caracteres ingresada:", cadena)
    print("Resultado cifrado:", resultado_cifrado)

def main():
    cadena = input("Ingresa la cadena de caracteres a cifrar: ")
    while(cadena==""):
        cadena = input("Ingresa la cadena de caracteres a cifrar: ")
        
    n = int(input("Ingresa el valor de desplazamiento (n): "))
    while(n <= 0):
        n = int(input("Ingresa el valor de desplazamiento válido (n): "))

    cifrado_monoalfabetico_desplazamiento(cadena, n)

if __name__ == "__main__":
    main()