import time
import random
import sympy

def generar_claves():
    # Paso 1: Generar dos números primos grandes
    p = sympy.randprime(2**10, 2**12)
    g = random.randint(2, p - 1)
    
    # Paso 2: Generar una clave privada aleatoria
    a = random.randint(2, p - 2)
    
    # Paso 3: Calcular la clave pública
    A = pow(g, a, p)
    
    return (p, g, A, a)

def cifrar_mensaje(mensaje, p, g, A):
    # Paso 4: Cifrar el mensaje
    k = random.randint(2, p - 2)
    K = pow(A, k, p)
    texto_cifrado = []
    for char in mensaje:
        m = ord(char)
        c1 = pow(g, k, p)
        c2 = (m * K) % p
        texto_cifrado.append((c1, c2))
    return texto_cifrado

def descifrar_mensaje(texto_cifrado, p, a):
    # Paso 5: Descifrar el mensaje
    texto_descifrado = ""
    for c1, c2 in texto_cifrado:
        s = pow(c1, a, p)
        m = (c2 * sympy.mod_inverse(s, p)) % p
        texto_descifrado += chr(m)
    return texto_descifrado

# Lista de archivos de texto
archivos = ["Mensaje_10.txt", "Mensaje_100.txt", "Mensaje_1000.txt", "Mensaje_10000.txt", 
            "Mensaje_100000.txt", "Mensaje_1000000.txt", "Mensaje_10000000.txt"]

for nombre_archivo in archivos:
    # Medición del tiempo de lectura del archivo
    start_time_lectura = time.time()
    with open("C:\\Users\\PC\\Documents\\pythonCripto\\DSA\\"+nombre_archivo, "r") as archivo:
        mensaje = archivo.read()
    tiempo_lectura = (time.time() - start_time_lectura) * 1000

    # Generar claves
    start_time_claves = time.time()
    p, g, A, a = generar_claves()
    tiempo_claves = (time.time() - start_time_claves) * 1000

    print("\nProcesando archivo:", nombre_archivo)
    print("Tiempo en leer el archivo:", tiempo_lectura, "milisegundos")
    print("Número de palabras:", len(mensaje.split()))
    print("Número de caracteres en el texto de entrada:", len(mensaje))
    print(f"Tiempo transcurrido en generación de claves: {tiempo_claves} milisegundos")

    # Cifrar el mensaje
    start_time_cifrado = time.time()
    texto_cifrado = cifrar_mensaje(mensaje, p, g, A)
    tiempo_cifrado = (time.time() - start_time_cifrado) * 1000

    print("Número de caracteres en el texto cifrado:", len(texto_cifrado))
    print(f"Tiempo transcurrido en cifrado: {tiempo_cifrado} milisegundos")

    # Descifrar el mensaje
    start_time_descifrado = time.time()
    texto_descifrado = descifrar_mensaje(texto_cifrado, p, a)
    tiempo_descifrado = (time.time() - start_time_descifrado) * 1000

    print("Número de caracteres en el texto descifrado:", len(texto_descifrado))
    print(f"Tiempo transcurrido en descifrado: {tiempo_descifrado} milisegundos")
