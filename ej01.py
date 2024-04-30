from itertools import permutations

def generar_anagramas(palabra):
    # Genera todas las permutaciones de la palabra
    lista_permutaciones = [''.join(p) for p in permutations(palabra)]
    lista_permutaciones.sort()  # Ordena alfabéticamente
    return lista_permutaciones

def main():
    
    palabra = input("Ingresa una palabra: ")
    while (palabra == ""):
        palabra = input("Ingresa una palabra: ")
    
    lista_permutaciones = generar_anagramas(palabra)
    
    print("Número total de permutaciones:", len(lista_permutaciones))
    print("Las 10 primeras permutaciones ordenadas alfabéticamente:")
    for i in range(min(10, len(lista_permutaciones))):
        print(lista_permutaciones[i])

if __name__ == "__main__":
    main()
