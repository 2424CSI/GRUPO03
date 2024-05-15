import time
import hashlib #operaciones de hash

#produce una salida de 160 bits,
#la clave generada tendrá una longitud de 40 caracteres en hexadecimal
#(160 bits / 4 bits por carácter = 40 caracteres).

def calcular_ripemd160(texto):

    inicio = time.perf_counter()  # Usamos perf_counter para mayor precisión
    
    hash_obj = hashlib.new('ripemd160')

    #independientemente de los caracteres utilizados en el texto original
    #los caracteres del texto se conviertan en una secuencia de bytes que la función hash puede procesar
    hash_obj.update(texto.encode('utf-8')) 

    resultado = hash_obj.hexdigest()
    fin = time.perf_counter()
    tiempo_transcurrido = (fin - inicio) * 1000  # Convertir a milisegundos
    return resultado, tiempo_transcurrido

def contar_palabras_y_caracteres(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    return num_palabras, num_caracteres

def main():
    # 1. Leer el archivo con el texto del mensaje a cifrar
    ruta_carpeta = 'C:/Users/denni/Documents/Octavo Semestre/Cripto/funcion hash/textos/'
    mensaje10 = 'mensaje10.txt'
    mensaje100 = 'mensaje100.txt'
    mensaje1000 = 'mensaje1000.txt'
    mensaje10000 = 'mensaje10000.txt'
    mensaje100000 = 'mensaje100000.txt'
    mensaje1000000 = 'mensaje1000000.txt'
    mensaje10000000 = 'mensaje10000000.txt'


    with open(ruta_carpeta + mensaje10000000, 'r') as archivo:
        mensaje = archivo.read()

    # Contar palabras y caracteres del texto de entrada
    num_palabras_entrada, num_caracteres_entrada = contar_palabras_y_caracteres(mensaje)

    # Medir tiempo de lectura del archivo
    inicio_lectura = time.perf_counter()
    clave, _ = calcular_ripemd160(mensaje)  # Solo necesitamos la clave, no el tiempo aquí
    fin_lectura = time.perf_counter()
    tiempo_lectura = (fin_lectura - inicio_lectura) * 1000  # Convertir a milisegundos
    print("Tiempo transcurrido para leer el archivo E1:", tiempo_lectura, "milisegundos")

    # 2. Generar e imprimir la clave de cifrado
    clave, tiempo_clave = calcular_ripemd160(mensaje)
    print("Clave de cifrado:", clave)
    print("Tiempo transcurrido para generar e imprimir la clave cifrada E2:", tiempo_clave, "milisegundos")

    # 3. Cifrar e imprimir el texto
    texto_cifrado, tiempo_cifrado = calcular_ripemd160(mensaje)
    print("Texto cifrado:", texto_cifrado)
    print("Tiempo transcurrido para cifrar el  E3:", tiempo_cifrado, "milisegundos")

    # Contar palabras y caracteres del texto cifrado
    num_palabras_salida, num_caracteres_salida = contar_palabras_y_caracteres(texto_cifrado)

    # Imprimir el número de palabras y caracteres de entrada y salida
    print("Número de palabras en el texto de entrada:", num_palabras_entrada)
    print("Número de caracteres en el texto de entrada:", num_caracteres_entrada)
    print("Número de caracteres en el texto cifrado:", num_caracteres_salida)

if __name__ == "__main__":
    main()
