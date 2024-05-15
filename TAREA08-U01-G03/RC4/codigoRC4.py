# Importar las bibliotecas necesarias
from Crypto.Cipher import ARC4
import time
import secrets

# Función para leer un archivo de texto y devolver su contenido como una cadena
def leer_archivo(nombre_archivo):
    inicio_lectura = time.time()  # Tiempo inicial de lectura
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read().replace(" ", "")  # Eliminar espacios en blanco
    tiempo_lectura = (time.time() - inicio_lectura) * 1000  # Tiempo en milisegundos
    print("Tiempo de lectura del archivo: {:.2f} milisegundos".format(tiempo_lectura))
    return contenido

# Función para generar una clave aleatoria
def generar_clave():
    inicio_generacion = time.time()  # Tiempo inicial de generación de clave
    clave = secrets.token_bytes(16)  # Genera una cadena de 16 bytes aleatorios
    tiempo_generacion = (time.time() - inicio_generacion) * 1000  # Tiempo en milisegundos
    print("Tiempo de generación de la clave: {:.2f} milisegundos".format(tiempo_generacion))
    return clave

# Función para cifrar un texto usando RC4
def cifrar_texto(texto, clave):
    inicio_cifrado = time.time()  # Tiempo inicial de cifrado
    cifrador = ARC4.new(clave)
    texto_cifrado = cifrador.encrypt(texto)
    tiempo_cifrado = (time.time() - inicio_cifrado) * 1000  # Tiempo en milisegundos
    print("Tiempo de cifrado: {:.2f} milisegundos".format(tiempo_cifrado))
    return texto_cifrado, tiempo_cifrado

# Función para descifrar un texto usando RC4
def descifrar_texto(texto_cifrado, clave):
    inicio_descifrado = time.time()  # Tiempo inicial de descifrado
    cifrador = ARC4.new(clave)
    texto_descifrado = cifrador.decrypt(texto_cifrado)
    tiempo_descifrado = (time.time() - inicio_descifrado) * 1000  # Tiempo en milisegundos
    print("Tiempo de descifrado: {:.2f} milisegundos".format(tiempo_descifrado))
    return texto_descifrado, tiempo_descifrado

# Nombre del archivo de texto
archivo_texto = "10000000palabras.txt"

# Leer el texto del archivo
texto_original = leer_archivo(archivo_texto)

# Generar una clave aleatoria
clave = generar_clave()
print("Clave de cifrado:", clave.hex())  # Imprimir la clave como una cadena hexadecimal

# Imprimir la longitud del texto original
print("Longitud del texto original:", len(texto_original))

# Cifrar el texto y calcular el tiempo transcurrido
texto_cifrado, tiempo_cifrado = cifrar_texto(texto_original.encode(), clave)

# Imprimir la longitud del texto cifrado
print("Longitud del texto cifrado:", len(texto_cifrado))

# Imprimir el mensaje cifrado
#print("Mensaje cifrado:", texto_cifrado)

# Descifrar el texto y calcular el tiempo transcurrido
texto_descifrado, tiempo_descifrado = descifrar_texto(texto_cifrado, clave)

# Imprimir el mensaje descifrado
#print("Mensaje descifrado:", texto_descifrado.decode())
