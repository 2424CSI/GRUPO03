import time
import hashlib

def whirlpool_hash(file_path):
    total_chars_read = 0  # Contador de caracteres leídos

    # Inicializamos el objeto hash Whirlpool dentro del contexto
    with open(file_path, "rb") as f:
        whirlpool = hashlib.new("whirlpool")
        
        start_read = time.time() # Tiempo de inicio de la lectura
        while True:
            # Leemos el archivo en bloques de 4096 bytes
            data = f.read(4096)
            if not data:
                break
            total_chars_read += len(data)  # Actualizamos el contador
            # Actualizamos el hash con los datos del archivo
            whirlpool.update(data)
        end_read = time.time() # Tiempo de fin de la lectura
    
    # Devolvemos el valor del hash, los tiempos y la cantidad de caracteres leídos
    hash_value = whirlpool.hexdigest()
    chars_hashed = len(hash_value)
    read_time = (end_read - start_read) * 1000
    return hash_value, read_time, total_chars_read, chars_hashed

if __name__ == "__main__":
    file_path = "Mensaje_10000000.txt"
    
    start_total = time.time() # Tiempo de inicio total
    
    try:
        hash_value, read_time, total_chars_read, chars_hashed = whirlpool_hash(file_path)
        print("Tiempo de lectura del archivo:", read_time, "milisegundos")
        print("Cantidad de caracteres leídos:", total_chars_read)
        print("Cantidad de caracteres del cifrado:", chars_hashed)
        print("Clave de cifrado (Whirlpool):", hash_value)
    except FileNotFoundError:
        print("Archivo no encontrado:", file_path)
    
    end_total = time.time() # Tiempo de fin total
    print("Tiempo total:", (end_total - start_total) * 1000, "milisegundos")
