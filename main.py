import pickle
import re
from enum import Enum
import os.path as path

class Libros(Enum):
    titulo = 0
    autor = 1
    isbn = 2
    categoria = 3
    estado = 4

class Usuarios(Enum):
    usuario = 0
    ci = 1
    fecha = 2
    titulo = 3
    isbn = 4

def MostrarLibros(arreglo):
    print()
    print("------------------------------Libros------------------------------")
    print()
    for i in range(len(arreglo)):
        print("Título: ", arreglo[i][Libros.titulo.value])
        print("Autor: ", arreglo[i][Libros.autor.value])
        print("ISBN: ", arreglo[i][Libros.isbn.value])
        print("Categoría: ", arreglo[i][Libros.categoria.value])
        print("Estado: ", arreglo[i][Libros.estado.value])
        print()
        print("------------------------------------------------------------------")
        print()

def OrdenarLibrosPorAutor(arreglo):
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j][Libros.autor.value] > clave[Libros.autor.value]:
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def OrdenarLibrosPorTitulo(arreglo):
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j][Libros.titulo.value] > clave[Libros.titulo.value]:
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def OrdenarLibrosPorCodigo(arreglo):
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and int(arreglo[j][Libros.isbn.value]) > int(clave[Libros.isbn.value]):
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def BusquedaBinariaLibroPorCodigo(codigo, arreglo, minimo, maximo):
    if maximo >= minimo:
        medio = (maximo + minimo) // 2
        if arreglo[medio][Libros.isbn.value] == codigo:
            return medio
        else:
            if arreglo[medio][Libros.isbn.value] > codigo:
                return BusquedaBinariaLibroPorCodigo(codigo, arreglo, minimo, medio - 1)
            else:
                return BusquedaBinariaLibroPorCodigo(codigo, arreglo, medio + 1, maximo)
    else:
        return -1

def BusquedaBinariaLibroPorNombre(codigo, arreglo, minimo, maximo):
    if maximo >= minimo:
        medio = (maximo + minimo) // 2
        if (arreglo[medio][Libros.titulo.value]).lower() == codigo:
            return medio
        else:
            if (arreglo[medio][Libros.titulo.value]).lower() > codigo:
                return BusquedaBinariaLibroPorNombre(codigo, arreglo, minimo, medio - 1)
            else:
                return BusquedaBinariaLibroPorNombre(codigo, arreglo, medio + 1, maximo)
    else:
        return -1

def InsertarLibroNuevo(nombre, arreglo):
    print()
    print("Usted está ingresando un libro nuevo. Deberá registrar los datos del mismo")
    print()
    libro = []
    libro.append(nombre)
    print("Autor: ", end = "")
    autor = input()
    libro.append(autor)
    isbn_mayor = arreglo[0][Libros.isbn.value]
    for i in range(len(arreglo)):
        if arreglo[i][Libros.isbn.value] > isbn_mayor:
            isbn_mayor = arreglo[i][Libros.isbn.value]
    libro.append(str(int(isbn_mayor) + 1))
    print("Categoría: ", end = "")
    categoria = input()
    libro.append(categoria)
    libro.append("Disponible")
    arreglo.append(libro)
    return arreglo

def VerificarFecha(fecha):
    if re.search(r"^\d{2}/\d{2}/\d{4}$", fecha) == None:
        return False
    else:
        return True
    
def VerificarCI(ci):
    if re.search(r"^\d{7,8}$", ci) == None:
        return False
    else:
        return True

def ImprimirDatosLibro(i, arr):
    print()
    if i == -1:
        print("Libro no encontrado")
    else:
        print("Título: ", arr[i][Libros.titulo.value])
        print("Autor: ", arr[i][Libros.autor.value])
        print("ISBN: ", arr[i][Libros.isbn.value])
        print("Categoría: ", arr[i][Libros.categoria.value])
        print("Estado: ", arr[i][Libros.estado.value])
    

def RetirarLibro(indice, libros, matriz_usuarios):
    usuario = []
    print()
    print("Ingrese los datos solicitados")
    print()
    print("Nombre de usuario: ", end = "")
    nombre = input()
    usuario.append(nombre)
    print("Cédula de Identidad: ", end = "")
    ci = input()
    verificar_ci = VerificarCI(ci)
    while not verificar_ci:
        print()
        print("CI inválida, debe tener entre 7 y 8 números (sin letras ni caracteres especiales)")
        print("Ingrese la Cédula de Identidad de nuevo: ", end = "")
        ci = input()
        verificar_ci = VerificarCI(ci)
    usuario.append(ci)
    print("Fecha actual (dd/mm/aaaa): ", end = "")
    fecha = input()
    verificar_fecha = VerificarFecha(fecha)
    while not verificar_fecha:
        print()
        print("Fecha inválida, debe  cumplir el formato especificado")
        print("Ingrese la fecha de nuevo:", end = "")
        fecha = input()
        verificar_fecha = VerificarFecha(fecha)
    usuario.append(fecha)
    usuario.append(libros[indice][Libros.titulo.value])
    usuario.append(libros[indice][Libros.isbn.value])
    matriz_usuarios.append(usuario)
    return matriz_usuarios

def MostrarPrestamos(arreglo):
    print()
    print("------------------------------Préstamos------------------------------")
    print()
    for i in range(len(arreglo)):
        print("Nombre de usuario: ", arreglo[i][Usuarios.usuario.value])
        print("C.I.: ", arreglo[i][Usuarios.ci.value])
        print("Fecha del préstamo: ", arreglo[i][Usuarios.fecha.value])
        print("Libro: ", arreglo[i][Usuarios.titulo.value])
        print("ISBN: ", arreglo[i][Usuarios.isbn.value])
        print()
        print("------------------------------------------------------------------")
        print()

def OrdenarUsuariosPorLibro(arreglo):
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j][Usuarios.titulo.value] > clave[Usuarios.titulo.value]:
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def OrdenarUsuariosPorCI(arreglo):
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and int(arreglo[j][Usuarios.ci.value]) > int(clave[Usuarios.ci.value]):
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def BusquedaBinariaUsuarioPorLibro(codigo, arreglo, minimo, maximo):
    if maximo >= minimo:
        medio = (maximo + minimo) // 2
        if (arreglo[medio][Usuarios.titulo.value]).lower() == codigo:
            return medio
        else:
            if (arreglo[medio][Usuarios.titulo.value]).lower() > codigo:
                return BusquedaBinariaUsuarioPorLibro(codigo, arreglo, minimo, medio - 1)
            else:
                return BusquedaBinariaUsuarioPorLibro(codigo, arreglo, medio + 1, maximo)
    else:
        return -1

def BusquedaLinealLibroPorCodigo(arreglo, objetivo):
    for i in range(len(arreglo)):
        if arreglo[i][Libros.isbn.value] == objetivo:
            return i
    return -1

def BusquedaLinealLibroPorNombre(arreglo, objetivo):
    for i in range(len(arreglo)):
        if arreglo[i][Libros.titulo.value].lower() == objetivo:
            return i
    return -1

def BusquedaLinealUsuarioPorLibro(arreglo, objetivo):
    for i in range(len(arreglo)):
        if arreglo[i][Usuarios.titulo.value].lower() == objetivo:
            return i
    return -1

def main():
    if  path.exists("libros.bin"):
        with open("libros.bin", "rb") as archivo_libros:
            matriz_libros = pickle.load(archivo_libros)
        if path.exists("usuarios.bin"):
            with open("usuarios.bin", "rb") as archivo_usuarios:
                matriz_usuarios = pickle.load(archivo_usuarios)
        else:
            matriz_usuarios = []
        libros_ordenados_isbn = False
        libros_ordenados_titulo = False
        libros_ordenados_autor = False
        usuarios_ordenados_libro = False
        usuarios_ordenados_ci = False
        print()
        print("------------------------------Menú------------------------------") 
        print("Escriba 1 para mostrar todo el inventario de libros")
        print("Escriba 2 para ordenar los libros por autor")
        print("Escriba 3 para ordenar los libros por título")
        print("Escriba 4 para ordenar los libros por código")
        print("Escriba 5 para buscar un libro por su código")
        print("Escriba 6 para buscar un libro por su nombre")
        print("Escriba 7 para ingresar un libro a la biblioteca")
        print("Escriba 8 para retirar un libro de la biblioteca")
        print("Escriba 9 para mostrar la lista de préstamos")
        print("Escriba 10 para ordenar el historial de préstamos por títulos")
        print("Escriba 11 para ordenar el historial de préstamos por CI")
        print("Escriba 0 para salir")
        respuesta = int(input())
        while(respuesta != 0):
            match(respuesta):
                case 1:
                    MostrarLibros(matriz_libros)
                case 2:
                    matriz_libros = OrdenarLibrosPorAutor(matriz_libros)
                    print()
                    print("Libros ordenados exitosamente")
                    print()
                    libros_ordenados_isbn = False
                    libros_ordenados_titulo = False
                    libros_ordenados_autor = True
                    with open("libros.bin", "wb") as archivo_libros:
                        pickle.dump(matriz_libros, archivo_libros)
                case 3:
                    matriz_libros = OrdenarLibrosPorTitulo(matriz_libros)
                    print()
                    print("Libros ordenados exitosamente")
                    print()
                    libros_ordenados_isbn = False
                    libros_ordenados_titulo = True
                    libros_ordenados_autor = False
                    with open("libros.bin", "wb") as archivo_libros:
                        pickle.dump(matriz_libros, archivo_libros)
                case 4:
                    matriz_libros = OrdenarLibrosPorCodigo(matriz_libros)
                    print()
                    print("Libros ordenados exitosamente")
                    print()
                    libros_ordenados_titulo = False
                    libros_ordenados_isbn = True
                    libros_ordenados_autor = False
                    with open("libros.bin", "wb") as archivo_libros:
                        pickle.dump(matriz_libros, archivo_libros)
                case 5:
                    print()
                    print("Ingrese el código ISBN del libro que desea buscar")
                    codigo = input()
                    print()
                    if libros_ordenados_isbn:
                        indice = BusquedaBinariaLibroPorCodigo(codigo, matriz_libros, 0, len(matriz_libros) - 1)
                        ImprimirDatosLibro(indice, matriz_libros)
                    else:
                        print("Es recomendable que primero ordene los libros por código para que el proceso sea más eficiente")
                        print("¿Desea Continuar? (S/N): ", end = "")
                        resp = input()
                        if resp.lower() == "s":
                            indice = BusquedaLinealLibroPorCodigo(matriz_libros, codigo)
                            ImprimirDatosLibro(indice, matriz_libros) 
                case 6:
                    print()
                    print("Ingrese el nombre del libro que desea buscar")
                    nombre = input()
                    nombre = nombre.lower()
                    nombre = re.sub("ñ", "n", nombre)
                    nombre = re.sub("á", "a", nombre)
                    nombre = re.sub("é", "e", nombre)
                    nombre = re.sub("í", "i", nombre)
                    nombre = re.sub("ó", "o", nombre)
                    nombre = re.sub("ü", "u", nombre)
                    nombre = re.sub("ú", "u", nombre)
                    print()
                    if libros_ordenados_titulo:
                        indice = BusquedaBinariaLibroPorNombre(nombre, matriz_libros, 0, len(matriz_libros) - 1)
                        ImprimirDatosLibro(indice, matriz_libros)
                    else:
                        print("Es recomendable que primero ordene los libros por título para que el proceso sea más eficiente")
                        print("¿Desea Continuar? (S/N): ", end = "")
                        resp = input()
                        if resp.lower() == "s":
                            indice = BusquedaLinealLibroPorNombre(matriz_libros, nombre)
                            ImprimirDatosLibro(indice, matriz_libros) 
                case 7:
                    print()
                    print("Ingrese el nombre del libro que desea ingresar")
                    nombre = input()
                    nombre = re.sub("ñ", "n", nombre)
                    nombre = re.sub("á", "a", nombre)
                    nombre = re.sub("é", "e", nombre)
                    nombre = re.sub("í", "i", nombre)
                    nombre = re.sub("ó", "o", nombre)
                    nombre = re.sub("ü", "u", nombre)
                    nombre = re.sub("ú", "u", nombre)
                    nombre = re.sub("Ñ", "N", nombre)
                    nombre = re.sub("Á", "A", nombre)
                    nombre = re.sub("É", "E", nombre)
                    nombre = re.sub("Í", "I", nombre)
                    nombre = re.sub("Ó", "O", nombre)
                    nombre = re.sub("Ú", "U", nombre)
                    nombre = re.sub("Ü", "U", nombre)
                    if libros_ordenados_titulo:
                        indice_libro = BusquedaBinariaLibroPorNombre(nombre.lower(), matriz_libros, 0, len(matriz_libros) - 1)
                    else:
                        print()
                        print("Es recomendable que primero ordene los libros por título para que el proceso sea más eficiente")
                        print("¿Desea Continuar? (S/N): ", end = "")
                        resp = input()
                        if resp.lower() == "s":
                            indice_libro = BusquedaLinealLibroPorNombre(matriz_libros, nombre.lower())
                        else:
                            indice_libro = -2
                    if indice_libro == -1:
                        matriz_libros = InsertarLibroNuevo(nombre, matriz_libros)
                        if libros_ordenados_isbn:
                            matriz_libros = OrdenarLibrosPorCodigo(matriz_libros)
                        if libros_ordenados_autor:
                            matriz_libros = OrdenarLibrosPorAutor(matriz_libros)
                        if libros_ordenados_titulo:
                            matriz_libros = OrdenarLibrosPorTitulo(matriz_libros)
                        with open("libros.bin", "wb") as archivo_libros:
                            pickle.dump(matriz_libros, archivo_libros)
                    else:
                        if (indice_libro > -1):
                            if matriz_libros[indice_libro][Libros.estado.value] == "Disponible":
                                print()
                                print("No puede ingresar el libro, porque este no está en el historial de préstamos")
                            else:
                                if usuarios_ordenados_libro:
                                    indice_usuario = BusquedaBinariaUsuarioPorLibro(nombre.lower(), matriz_usuarios, 0, len(matriz_usuarios) - 1)
                                else:
                                    print()
                                    print("Es recomendable que primero ordene los préstamos por título para que el proceso sea más eficiente")
                                    print("¿Desea Continuar? (S/N): ", end = "")
                                    resp = input()
                                    if resp.lower() == "s":
                                        indice_usuario = BusquedaLinealUsuarioPorLibro(matriz_usuarios, nombre.lower())
                                    else:
                                        indice_usuario = -2
                                if indice_usuario != -2:
                                    print()
                                    print("Ingrese su Cédula de Identidad: ", end = "")
                                    cedula = input()
                                    if matriz_usuarios[indice_usuario][Usuarios.ci.value] == cedula:
                                        matriz_libros[indice_libro][Libros.estado.value] = "Disponible"
                                        matriz_usuarios.pop(indice_usuario)
                                        with open("usuarios.bin", "wb") as archivo_usuarios:
                                            pickle.dump(matriz_usuarios, archivo_usuarios)
                                        with open("libros.bin", "wb") as archivo_libros:
                                            pickle.dump(matriz_libros, archivo_libros)
                                    else:
                                        print()
                                        print("No puede ingresar el libro, porque usted no dispone del mismo")   
                case 8:
                    print()
                    print("Ingrese el nombre del libro que desea retirar")
                    nombre = (input()).lower()
                    nombre = re.sub("ñ", "n", nombre)
                    nombre = re.sub("á", "a", nombre)
                    nombre = re.sub("é", "e", nombre)
                    nombre = re.sub("í", "i", nombre)
                    nombre = re.sub("ó", "o", nombre)
                    nombre = re.sub("ü", "u", nombre)
                    nombre = re.sub("ú", "u", nombre)
                    if libros_ordenados_titulo:
                        indice = BusquedaBinariaLibroPorNombre(nombre, matriz_libros, 0, len(matriz_libros) - 1)
                    else:
                        print()
                        print("Es recomendable que primero ordene los libros por título para que el proceso sea más eficiente")
                        print("¿Desea Continuar? (S/N): ", end = "")
                        resp = input()
                        if resp.lower() == "s":
                            indice = BusquedaLinealLibroPorNombre(matriz_libros, nombre)
                        else:
                            indice = -2
                    if indice == -1:
                        print()
                        print("El libro no está en el catálogo")
                    else:
                        if indice > -1:
                            if matriz_libros[indice][Libros.estado.value] == "Prestado":
                                print()
                                print("El libro está prestado a uno de nuestros usuarios. Vuelva pronto")
                            else:
                                matriz_libros[indice][Libros.estado.value] = "Prestado"
                                matriz_usuarios = RetirarLibro(indice, matriz_libros, matriz_usuarios)
                                if usuarios_ordenados_ci:
                                    matriz_usuarios = OrdenarUsuariosPorCI(matriz_usuarios)
                                if usuarios_ordenados_libro:
                                    matriz_usuarios = OrdenarUsuariosPorLibro(matriz_usuarios)
                                with open("usuarios.bin", "wb") as archivo_usuarios:
                                    pickle.dump(matriz_usuarios, archivo_usuarios)
                                with open("libros.bin", "wb") as archivo_libros:
                                    pickle.dump(matriz_libros, archivo_libros)
                case 9:
                    MostrarPrestamos(matriz_usuarios)
                case 10:
                    matriz_usuarios = OrdenarUsuariosPorLibro(matriz_usuarios)
                    print()
                    print("Préstamos ordenados exitosamente")
                    print()
                    with open("usuarios.bin", "wb") as archivo_usuarios:
                        pickle.dump(matriz_usuarios, archivo_usuarios)
                    usuarios_ordenados_ci = False
                    usuarios_ordenados_libro = True
                case 11:
                    matriz_usuarios = OrdenarUsuariosPorCI(matriz_usuarios)
                    print()
                    print("Préstamos ordenados exitosamente")
                    print()
                    with open("usuarios.bin", "wb") as archivo_usuarios:
                        pickle.dump(matriz_usuarios, archivo_usuarios)
                    usuarios_ordenados_ci = True
                    usuarios_ordenados_libro = False
            print()
            print("------------------------------Menú------------------------------") 
            print("Escriba 1 para mostrar todo el inventario")
            print("Escriba 2 para ordenar los libros por autor")
            print("Escriba 3 para ordenar los libros por título")
            print("Escriba 4 para ordenar los libros por código")
            print("Escriba 5 para buscar un libro por su código")
            print("Escriba 6 para buscar un libro por su nombre")
            print("Escriba 7 para ingresar un libro a la biblioteca")
            print("Escriba 8 para retirar un libro de la biblioteca")
            print("Escriba 9 para mostrar la lista de préstamos")
            print("Escriba 10 para ordenar el historial de préstamos por títulos")
            print("Escriba 11 para ordenar el historial de préstamos por CI")
            print("Escriba 0 para salir")
            respuesta = int(input())
    else:
        print()
        print("ERROR. No se ha podido abrir el archivo")
        print()
    print()
    print("FIN DEL PROGRAMA")
    print()
main()