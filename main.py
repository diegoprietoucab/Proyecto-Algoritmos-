import pickle                          #se importan las librerías necesarias
import re
from enum import Enum
import os.path as path

class Libros(Enum):                     #dato de tipo enumerado para los libros
    titulo = 0
    autor = 1
    isbn = 2
    categoria = 3
    estado = 4

class Usuarios(Enum):                    #dato de tipo enumerado par los usuarios
    usuario = 0
    ci = 1
    fecha = 2
    titulo = 3
    isbn = 4

def MostrarLibros(arreglo):             #función para mostrar todos los libros
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

def OrdenarLibrosPorAutor(arreglo):         #función para ordenar los libros por autor (Insertion Sort)
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j][Libros.autor.value].lower() > clave[Libros.autor.value].lower():
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def OrdenarLibrosPorTitulo(arreglo):       #función para ordenar los libros por título (Insertion Sort)
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j][Libros.titulo.value].lower() > clave[Libros.titulo.value].lower():
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def OrdenarLibrosPorCodigo(arreglo):        #función para ordenar los libros por código (Insertion Sort)
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and int(arreglo[j][Libros.isbn.value]) > int(clave[Libros.isbn.value]):
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def BusquedaBinariaLibroPorCodigo(codigo, arreglo, minimo, maximo):         #función para buscar los libros por código (Búsqueda Binaria)
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

def BusquedaBinariaLibroPorNombre(codigo, arreglo, minimo, maximo):         #función para buscar los libros por nombre (Búsqueda Binaria)
    if maximo >= minimo:
        medio = (maximo + minimo) // 2
        if (arreglo[medio][Libros.titulo.value]).lower() == codigo.lower():
            return medio
        else:
            if (arreglo[medio][Libros.titulo.value]).lower() > codigo.lower():
                return BusquedaBinariaLibroPorNombre(codigo, arreglo, minimo, medio - 1)
            else:
                return BusquedaBinariaLibroPorNombre(codigo, arreglo, medio + 1, maximo)
    else:
        return -1

def InsertarLibroNuevo(nombre, arreglo):                                                    #función para ingresar libro nuevo
    print()
    print("Usted está ingresando un libro nuevo. Deberá registrar los datos del mismo")
    print()
    libro = []
    libro.append(nombre)                                                    #se agrega el nombre del libro a un arreglo llamado
    print("Autor: ", end = "")                                                      
    autor = input()
    libro.append(autor)                                                    #se agrega el autor introducido por teclado al arreglo
    isbn_mayor = arreglo[0][Libros.isbn.value]                             #se declara arbitrariamente el isbn mayor como el del primer libro
    for i in range(len(arreglo)):                                          #se recorre toda la matriz
        if arreglo[i][Libros.isbn.value] > isbn_mayor:                     #si el isbn del libro actual es mayor 
            isbn_mayor = arreglo[i][Libros.isbn.value]                     #se reemplaza el valor de la variable del isbn mayor por el nuevo isbn
    libro.append(str(int(isbn_mayor) + 1))                                 #se agrega el isbn al arreglo
    print("Categoría: ", end = "")
    categoria = input()
    libro.append(categoria)                                                #se agrega la categoría introducida por teclado al arreglo
    libro.append("Disponible")                                             #se agrega el estado del libro como disponible
    arreglo.append(libro)                                                  #se agrega el arreglo del libro a la matriz principal
    return arreglo

def VerificarFecha(fecha):                                            #función de verificación de fechas
    if re.search(r"^\d{2}/\d{2}/\d{4}$", fecha) == None:              #expresion regular para confirmar formato dd/mm/aaaa
        return False
    else:
        return True
    
def VerificarCI(ci):                                                  #función para verificar Cédula de identidad
    if re.search(r"^\d{1,}$", ci) == None:                            #expresión regular para confirmar formato numérico
        return False
    else:
        return True

def ImprimirDatosLibro(i, arr):                                      #función para imprimir los datos de un solo libro
    print()
    if i == -1:
        print("Libro no encontrado")                                 #mensaje mostrado si el libro no es encontrado
    else:
        print("Título: ", arr[i][Libros.titulo.value])
        print("Autor: ", arr[i][Libros.autor.value])
        print("ISBN: ", arr[i][Libros.isbn.value])
        print("Categoría: ", arr[i][Libros.categoria.value])
        print("Estado: ", arr[i][Libros.estado.value])
    

def RetirarLibro(indice, libros, matriz_usuarios):                  #función para retirar un libro
    usuario = []
    print()
    print("Ingrese los datos solicitados")                          #se dolicitan todos los datos del usuario y se guardan en un arreglo
    print()
    print("Nombre de usuario: ", end = "")
    nombre = input()
    usuario.append(nombre)
    print("Cédula de Identidad: ", end = "")
    ci = input()
    verificar_ci = VerificarCI(ci)                                  #se verifica el formato de la cédula
    while not verificar_ci:
        print()
        print("CI inválida, debe tener solo números (sin letras ni caracteres especiales)")
        print("Ingrese la Cédula de Identidad de nuevo: ", end = "")
        ci = input()
        verificar_ci = VerificarCI(ci)
    usuario.append(ci)
    print("Fecha actual (dd/mm/aaaa): ", end = "")         
    fecha = input()
    verificar_fecha = VerificarFecha(fecha)                        #se verifica el formato de la fecha
    while not verificar_fecha:
        print()
        print("Fecha inválida, debe  cumplir el formato especificado")
        print("Ingrese la fecha de nuevo:", end = "")
        fecha = input()
        verificar_fecha = VerificarFecha(fecha)
    usuario.append(fecha)
    usuario.append(libros[indice][Libros.titulo.value])    #se agregan el título y el isbn con el índice de la función de búsqueda usada previamente
    usuario.append(libros[indice][Libros.isbn.value])
    matriz_usuarios.append(usuario)                        #se arregla el arreglo a la matriz principal de préstamos / usuarios
    return matriz_usuarios

def MostrarPrestamos(arreglo):                                                        #función para mostrar todos los préstamos
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

def OrdenarUsuariosPorLibro(arreglo):                      #función para ordenar los usuarios por libro (Insertion Sort)
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j][Usuarios.titulo.value].lower() > clave[Usuarios.titulo.value].lower():
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def OrdenarUsuariosPorCI(arreglo):                         #función para ordenar los usuarios por CI (Insertion Sort)
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and int(arreglo[j][Usuarios.ci.value]) > int(clave[Usuarios.ci.value]):
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = clave
    return arreglo

def BusquedaBinariaUsuarioPorLibro(codigo, arreglo, minimo, maximo):        #función para buscar un usuario por libro (Búsqueda Binaria)
    if maximo >= minimo:
        medio = (maximo + minimo) // 2
        if (arreglo[medio][Usuarios.titulo.value]).lower() == codigo.lower():
            return medio
        else:
            if (arreglo[medio][Usuarios.titulo.value]).lower() > codigo.lower():
                return BusquedaBinariaUsuarioPorLibro(codigo, arreglo, minimo, medio - 1)
            else:
                return BusquedaBinariaUsuarioPorLibro(codigo, arreglo, medio + 1, maximo)
    else:
        return -1

def BusquedaLinealLibroPorCodigo(arreglo, objetivo):            #función para buscar un libro por código (Búsqueda Lineal)
    for i in range(len(arreglo)):
        if arreglo[i][Libros.isbn.value] == objetivo:
            return i
    return -1

def BusquedaLinealLibroPorNombre(arreglo, objetivo):            #función para buscar un libro por nombre (Búsqueda Lineal)
    for i in range(len(arreglo)):
        if arreglo[i][Libros.titulo.value].lower() == objetivo:
            return i
    return -1

def BusquedaLinealUsuarioPorLibro(arreglo, objetivo):           #función para buscar un libro por usuario
    for i in range(len(arreglo)):
        if arreglo[i][Usuarios.titulo.value].lower() == objetivo:
            return i
    return -1

def main():                                                                  #función principal
    if  path.exists("libros.bin"):                                           #la función principal se ejecutará sólo si el archivo libros.bin existe                 
        with open("libros.bin", "rb") as archivo_libros:
            matriz_libros = pickle.load(archivo_libros)                      #se descarga la matriz de libros
        if path.exists("usuarios.bin"):                               
            with open("usuarios.bin", "rb") as archivo_usuarios:
                matriz_usuarios = pickle.load(archivo_usuarios)              #se descarga la matriz de usuarios sólo si usuarios.bin existe
        else:
            matriz_usuarios = []                                             #en caso contrarios la matriz de usuarios estará vacía
        libros_ordenados_isbn = False
        libros_ordenados_titulo = False
        libros_ordenados_autor = False
        usuarios_ordenados_libro = False
        usuarios_ordenados_ci = False
        print()
        print("------------------------------Menú------------------------------")          #se muestra el menú de opciones
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
        while(respuesta != 0):                                #mientras la respuesta sea distinta a cero
            match(respuesta):                                 #se ejecutará la función solicitada por el usuario y se mostrará de nuevo el menú
                case 1:
                    MostrarLibros(matriz_libros)              #se muestran todos los libros
                case 2:
                    matriz_libros = OrdenarLibrosPorAutor(matriz_libros)          #se ordenan los libros por autor
                    print()
                    print("Libros ordenados exitosamente")
                    print()
                    libros_ordenados_isbn = False
                    libros_ordenados_titulo = False
                    libros_ordenados_autor = True
                    with open("libros.bin", "wb") as archivo_libros:
                        pickle.dump(matriz_libros, archivo_libros)                #se reescribe el archivo libros.bin con los nuevos cambios
                case 3:
                    matriz_libros = OrdenarLibrosPorTitulo(matriz_libros)           #se ordenan los libros por título
                    print()
                    print("Libros ordenados exitosamente")
                    print()
                    libros_ordenados_isbn = False
                    libros_ordenados_titulo = True
                    libros_ordenados_autor = False
                    with open("libros.bin", "wb") as archivo_libros:
                        pickle.dump(matriz_libros, archivo_libros)                #se reescribe el archivo libros.bin con los nuevos cambios
                case 4:
                    matriz_libros = OrdenarLibrosPorCodigo(matriz_libros)        #se ordenan los libros por código
                    print()
                    print("Libros ordenados exitosamente")
                    print()
                    libros_ordenados_titulo = False
                    libros_ordenados_isbn = True
                    libros_ordenados_autor = False
                    with open("libros.bin", "wb") as archivo_libros:
                        pickle.dump(matriz_libros, archivo_libros)                #se reescribe el archivo libros.bin con los nuevos cambios
                case 5:
                    print()
                    print("Ingrese el código ISBN del libro que desea buscar") 
                    codigo = input()
                    print()                                  #se realiza la búsqueda de libros por código y se imprimen los datos del libro correspondiente
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
                    nombre = re.sub("ñ", "n", nombre)                 #se sustituyen las letras con acento y las ñ
                    nombre = re.sub("á", "a", nombre)
                    nombre = re.sub("é", "e", nombre)
                    nombre = re.sub("í", "i", nombre)
                    nombre = re.sub("ó", "o", nombre)
                    nombre = re.sub("ü", "u", nombre)
                    nombre = re.sub("ú", "u", nombre)
                    print()                               #se realiza la búsqueda de libros por nombre y se imprimen los datos del libro correspondiente
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
                    nombre = input()                                #se lee el libro que se quiere ingresar
                    nombre = re.sub("ñ", "n", nombre)               #se sustituyen los las letras con acento y las ñ
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
                        indice_libro = BusquedaBinariaLibroPorNombre(nombre.lower(), matriz_libros, 0, len(matriz_libros) - 1)  #se realiza la búsqueda de libros por nombre
                    else:
                        print()
                        print("Es recomendable que primero ordene los libros por título para que el proceso sea más eficiente")
                        print("¿Desea Continuar? (S/N): ", end = "")
                        resp = input()
                        if resp.lower() == "s":
                            indice_libro = BusquedaLinealLibroPorNombre(matriz_libros, nombre.lower())  #se realiza la búsqueda de libros por nombre
                        else:
                            indice_libro = -2
                    if indice_libro == -1:                                          #si el libro no se encuentra en la matriz de libros
                        matriz_libros = InsertarLibroNuevo(nombre, matriz_libros)   #se ejecuta la función para insertar un libro nuevo a la matriz
                        if libros_ordenados_isbn:
                            matriz_libros = OrdenarLibrosPorCodigo(matriz_libros)
                        if libros_ordenados_autor:
                            matriz_libros = OrdenarLibrosPorAutor(matriz_libros)
                        if libros_ordenados_titulo:
                            matriz_libros = OrdenarLibrosPorTitulo(matriz_libros)
                        with open("libros.bin", "wb") as archivo_libros:
                            pickle.dump(matriz_libros, archivo_libros)                 #se reescribe el archivo libros.bin con los nuevos cambios
                    else:
                        if (indice_libro > -1):                                                      #si el libro se encuentra en la matriz de libros se realizará una devolución
                            if matriz_libros[indice_libro][Libros.estado.value] == "Disponible":     #si el estado del libro es Disponible, no lo puede retornar ya que no ha sido prestado 
                                print()
                                print("No puede ingresar el libro, porque este no está en el historial de préstamos")
                            else:
                                if usuarios_ordenados_libro:                                                                                        #en caso contrario
                                    indice_usuario = BusquedaBinariaUsuarioPorLibro(nombre.lower(), matriz_usuarios, 0, len(matriz_usuarios) - 1)   #se realiza una búsqueda de usuario por libro
                                else:
                                    print()
                                    print("Es recomendable que primero ordene los préstamos por título para que el proceso sea más eficiente")
                                    print("¿Desea Continuar? (S/N): ", end = "")
                                    resp = input()
                                    if resp.lower() == "s":
                                        indice_usuario = BusquedaLinealUsuarioPorLibro(matriz_usuarios, nombre.lower())       #se realiza una búsqueda de usuario por libro
                                    else:
                                        indice_usuario = -2
                                if indice_usuario != -2:
                                    print()
                                    print("Ingrese su Cédula de Identidad: ", end = "")                  #se le solicita la cédula al usuario
                                    cedula = input()                                                     #si la cédula introducida es igual a la cédula del usuario del índice retornado por la búsqueda
                                    if matriz_usuarios[indice_usuario][Usuarios.ci.value] == cedula:     #el usuario dispone del libro
                                        matriz_libros[indice_libro][Libros.estado.value] = "Disponible"  #se cambia el estado del libro a disponible
                                        matriz_usuarios.pop(indice_usuario)                              #se elimina el usuario de la matriz de préstamos
                                        with open("usuarios.bin", "wb") as archivo_usuarios:
                                            pickle.dump(matriz_usuarios, archivo_usuarios)    #se reescribe el archivo usuarios.bin con los nuevos cambios
                                        with open("libros.bin", "wb") as archivo_libros:      
                                            pickle.dump(matriz_libros, archivo_libros)        #se reescribe el archivo libros.bin con los nuevos cambios
                                    else:
                                        print()
                                        print("No puede ingresar el libro, porque usted no dispone del mismo")     #mensaje mostrado si el usuario no tiene el libro que quiere devolver
                case 8:
                    print()
                    print("Ingrese el nombre del libro que desea retirar")
                    nombre = (input()).lower()                               #se lee el libro que se desea retirar
                    nombre = re.sub("ñ", "n", nombre)
                    nombre = re.sub("á", "a", nombre)
                    nombre = re.sub("é", "e", nombre)
                    nombre = re.sub("í", "i", nombre)
                    nombre = re.sub("ó", "o", nombre)
                    nombre = re.sub("ü", "u", nombre)
                    nombre = re.sub("ú", "u", nombre)
                    if libros_ordenados_titulo:
                        indice = BusquedaBinariaLibroPorNombre(nombre, matriz_libros, 0, len(matriz_libros) - 1)   #se realiza la búsqueda de libros por nombre
                    else:
                        print()
                        print("Es recomendable que primero ordene los libros por título para que el proceso sea más eficiente")
                        print("¿Desea Continuar? (S/N): ", end = "")
                        resp = input()
                        if resp.lower() == "s":
                            indice = BusquedaLinealLibroPorNombre(matriz_libros, nombre)   #se realiza la búsqueda de libros por nombre
                        else:
                            indice = -2
                    if indice == -1:
                        print()
                        print("El libro no está en el catálogo")    #mensaje a mostrar si el libro no se encuentra
                    else:
                        if indice > -1:
                            if matriz_libros[indice][Libros.estado.value] == "Prestado":       #si el libro está en el catálogo se cambia su estado a prestado
                                print()
                                print("El libro está prestado a uno de nuestros usuarios. Vuelva pronto")
                            else:
                                matriz_libros[indice][Libros.estado.value] = "Prestado"
                                matriz_usuarios = RetirarLibro(indice, matriz_libros, matriz_usuarios)     #se ejecuta la función para retirar libros
                                if usuarios_ordenados_ci:
                                    matriz_usuarios = OrdenarUsuariosPorCI(matriz_usuarios)
                                if usuarios_ordenados_libro:
                                    matriz_usuarios = OrdenarUsuariosPorLibro(matriz_usuarios)
                                with open("usuarios.bin", "wb") as archivo_usuarios:
                                    pickle.dump(matriz_usuarios, archivo_usuarios)    #se reescribe el archivo usuarios.bin con los nuevos cambios
                                with open("libros.bin", "wb") as archivo_libros:
                                    pickle.dump(matriz_libros, archivo_libros)        #se reescribe el archivo libros.bin con los nuevos cambios
                case 9:
                    MostrarPrestamos(matriz_usuarios)                                #se muestran todos los préstamos
                case 10:
                    matriz_usuarios = OrdenarUsuariosPorLibro(matriz_usuarios)      #se ordenan los préstamos por libro
                    print()
                    print("Préstamos ordenados exitosamente")
                    print()
                    with open("usuarios.bin", "wb") as archivo_usuarios:
                        pickle.dump(matriz_usuarios, archivo_usuarios)              #se reescribe el archivo usuarios.bin con los nuevos cambios
                    usuarios_ordenados_ci = False
                    usuarios_ordenados_libro = True
                case 11:
                    matriz_usuarios = OrdenarUsuariosPorCI(matriz_usuarios)         #se ordenan los préstamos por cédula
                    print()
                    print("Préstamos ordenados exitosamente")
                    print()
                    with open("usuarios.bin", "wb") as archivo_usuarios:
                        pickle.dump(matriz_usuarios, archivo_usuarios)             #se reescribe el archivo usuarios.bin con los nuevos cambios
                    usuarios_ordenados_ci = True
                    usuarios_ordenados_libro = False
            print()
            print("------------------------------Menú------------------------------")      #se muestra el menú
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
        print("ERROR. No se ha podido abrir el archivo")               #mensaje que se mmuestra si no se puede abrir libros.bin
        print()
    print()
    print("FIN DEL PROGRAMA")                                          #mensaje que se muestra al finalizar el programa
    print()
main()