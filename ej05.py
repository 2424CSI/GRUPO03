import string

def cifrado_vigenere(mensaje, clave):
    alfabeto = string.ascii_uppercase
    mensaje_cifrado = ''
    clave_repetida = clave * (len(mensaje) // len(clave)) + clave[:len(mensaje) % len(clave)]
    print(clave_repetida)

    for i in range(len(mensaje)):
        if mensaje[i].upper() in alfabeto:
            mensaje_cifrado += alfabeto[(alfabeto.index(mensaje[i].upper()) + alfabeto.index(clave_repetida[i].upper())) % 26]
        else:
            mensaje_cifrado += mensaje[i]

    return mensaje_cifrado

def main():
    
    mensaje = input("Ingresa la cadena de caracteres a cifrar: ")
    while (mensaje == ""):
        mensaje = input("Ingresa la cadena de caracteres a cifrar: ")
        
    clave = input("Ingresa la clave de cifrado: ")
    
    while (clave == ""):
        clave = input("Ingresa la clave de cifrado:  ")

    mensaje_cifrado = cifrado_vigenere(mensaje, clave)

    print("Cadena de caracteres ingresada:", mensaje)
    print("Clave de cifrado:", clave)
    print("Cadena de caracteres cifrada:", mensaje_cifrado)

if __name__ == "__main__":
    main()