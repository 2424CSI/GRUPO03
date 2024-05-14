import random
import string

def generate_words(n):
    words = []
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))
        words.append(word)
    return words

def save_to_file(words, filename):
    with open(filename, 'w') as f:
        f.write(' '.join(words))

def generate_text_files():
    #sizes = [10000000]
    sizes = [10, 100, 1000,10000,100000,1000000,10000000]
    for size in sizes:
        words = generate_words(size)
        filename = f"Mensaje_{size}.txt"
        save_to_file(words, filename)
        print(f"Archivo '{filename}' generado con éxito.")

if __name__ == "__main__":
    generate_text_files()
