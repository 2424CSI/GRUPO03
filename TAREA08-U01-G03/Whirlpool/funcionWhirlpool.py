import time
import hashlib

def encrypt_whirlpool(data):
    # Calcula el tiempo en generar el mensaje cifrado
    start_time = time.time()
    hash_obj = hashlib.new("whirlpool")
    hash_obj.update(data.encode("utf-8"))
    encrypted_message = hash_obj.hexdigest()
    end_time = time.time()
    generation_time = end_time - start_time
    return encrypted_message, generation_time

def main():
    # Leer el archivo de texto
    file_name = "MensajeT_10.txt"
    with open(file_name, "r") as file:
        input_text = file.read()

    # Calcula el tiempo en leer el archivo y la cantidad de caracteres de entrada
    input_length = len(input_text)
    start_time = time.time()
    encrypted_message, generation_time = encrypt_whirlpool(input_text)
    end_time = time.time()
    read_time = end_time - start_time

    # Calcula el tiempo en cifrar el mensaje y el número de caracteres de salida
    encryption_time = end_time - start_time
    output_length = len(encrypted_message)

    # Tiempo total
    total_time = read_time + generation_time + encryption_time

    # Imprimir resultados
    print("Tiempo en leer el archivo:", read_time, "segundos")
    print("Cantidad de caracteres de entrada:", input_length)
    print("Tiempo en generar el mensaje cifrado:", generation_time, "segundos")
    print("Tiempo en cifrar el mensaje:", encryption_time, "segundos")
    print("Número de caracteres de salida:", output_length)
    print("Tiempo total:", total_time, "segundos")

if __name__ == "__main__":
    main()
