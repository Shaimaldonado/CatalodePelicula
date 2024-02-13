from CatalogodePelicula1 import*
opcion = None
nombre_catalogo = input("Ingresaste al catalogo de peliculas, ingresa ENTER para seguir navegando")
catalogo = CatalogodePeliculas(nombre_catalogo)

while opcion != 4:
    print("\nOpciones:")
    print("1: Agregar pelicula")
    print("2: Ver lista de peliculas")
    print("3: Eliminar pelicula del catalogo")
    print("4: Salir del catalogo")
    
    opcion = int(input("Elige una de las siguientes opciones: "))
    
    if opcion == 1:
        nombre_pelicula = input("Nombre de la pelicula que estas buscando: ")
        pelicula = Pelicula(nombre_pelicula)
        catalogo.agregar_pelicula(pelicula)
    elif opcion == 2:
        catalogo.listar_peliculas()
    elif opcion == 3:
        catalogo.eliminar_peliculas()
    elif opcion == 4:
        print("Saliste del catalogo.")
    else:
        print("Marcaste una opcion incorrecta, internta nuevamente.")