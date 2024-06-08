import pickle

matriz = []

try:
    arch = open("Libros.txt", "rt")
    x = arch.readlines()
    arch.close()
    with open("Libros.txt", "rt") as arch:
        for i in range(len(x) // 5):
            fila = []
            for j in range(5):
                fila.append((arch.readline()).removesuffix("\n"))
            matriz.append(fila)
    with open("libros.bin", "wb") as arch:
        pickle.dump(matriz, arch)
    print()
    print("Archivo creado con éxito")
    print()
except:
    print()
    print("ERROR. No se pudo abrir el archivo")
    print()