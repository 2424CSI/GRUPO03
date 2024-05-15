import time
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def generar_clave():
    start_time = time.time()
    clave = DSA.generate(2048)
    end_time = time.time()
    print("Clave generada:", clave)
    print("Tiempo para generar la clave: {:.6f} milisegundos".format((end_time - start_time)*1000))
    return clave

def cifrar_mensaje(clave, mensaje):
    start_time = time.time()
    h = SHA256.new(mensaje)
    firmador = DSS.new(clave, 'fips-186-3')
    firma = firmador.sign(h)
    end_time = time.time()
    print("Tiempo para cifrar el mensaje: {:.6f} milisegundos".format((end_time - start_time)*1000))
    return firma

def descifrar_mensaje(clave, firma, mensaje):
    start_time = time.time()
    h = SHA256.new(mensaje)
    verificador = DSS.new(clave, 'fips-186-3')
    try:
        verificador.verify(h, firma)
        end_time = time.time()
        print("Tiempo para descifrar el mensaje: {:.6f} milisegundos".format((end_time - start_time)*1000))
        return True
    except ValueError:
        return False

def main():
    archivos = ["Mensaje_10.txt", "Mensaje_100.txt", "Mensaje_1000.txt", "Mensaje_10000.txt", 
                "Mensaje_100000.txt", "Mensaje_1000000.txt", "Mensaje_10000000.txt"]

    for archivo in archivos:
        start_time_read = time.time()
        with open("C:\\Users\\PC\\Documents\\pythonCripto\\DSA\\"+archivo, "r") as f:
            mensaje = f.read().encode()
        tiempo_lectura = (time.time() - start_time_read)* 1000

        print("\nProcesando archivo:", archivo)
        print("Tiempo en leer el archivo:", tiempo_lectura, "milisegundos")
        print("Número de palabras:", len(mensaje.split()))
        print("Número de caracteres en el texto de entrada:", len(mensaje))

        clave = generar_clave()
        firma = cifrar_mensaje(clave, mensaje)
        descifrado = descifrar_mensaje(clave.public_key(), firma, mensaje)
        print("Número de caracteres en el texto cifrado:", len(firma))

        if descifrado:
            print("El texto fue correctamente descifrado.")
        else:
            print("Error: La firma no coincide.")

if __name__ == "__main__":
    main()
