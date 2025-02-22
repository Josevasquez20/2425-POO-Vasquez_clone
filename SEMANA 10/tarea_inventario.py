class Item:  # Creamos nuestra clase Item
    def __init__(self, id_item, nombre, cantidad, precio):  # Constructor con atributos
        self.id_item = id_item
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):  #Metodo para el id
        return self.id_item

    def get_nombre(self):  # metodo para el nombre
        return self.nombre

    def get_cantidad(self):  # metodo para obtener la cantidad
        return self.cantidad

    def get_precio(self):  # metodo para obtener el precio
        return self.precio

    def set_cantidad(self, cantidad):  # metodo para establecer la cantidad
        self.cantidad = cantidad

    def set_precio(self, precio):  # metodo para establecer el precio
        self.precio = precio


class Inventario:

    def __init__(self):
        self.items = [] # Creamos una lista vacía para almacenar los productos
        self.archivo = "inventario.txt"  # Definimos el nombre del archivo donde se guardará el inventario
        self.cargar_archivo() # # Llamamos al metodo para cargar datos del archivo cuando se crea el inventario

    #Creamos el metodo para guardar el archivo
    def guardar_archivo(self):
        try:
            with open(self.archivo, "w") as f:  # Abrimos el archivo en modo escritura w
                for item in self.items:   # Recorremos cada producto en la lista
                    f.write(f"{item.get_id()},{item.get_nombre()},{item.get_cantidad()},{item.get_precio()}\n")  ## Escribimos cada producto en una línea del archivo, separando los datos con comas
            print("Cambios guardados en archivo.")  #Imprimimos si los cambios se guardan
        except: # Si ocurre cualquier error
            print("Error al guardar en archivo.")  #Imprimimos que hubo un error al guardar
    #Creamos un metodo para cargar el archivo
    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:  # Abrimos  el archivo en modo lectura r
                for linea in f: #Recorremos el archi linea por linea
                    datos = linea.strip().split(",")  # Eliminamos espacios y dividimos  la línea por comas
                    item = Item(datos[0], datos[1], int(datos[2]), float(datos[3]))  # Creamos un nuevo Item con los datos de la línea
                    self.items.append(item) # Añadimos el item a la lista
            print("Inventario cargado del archivo.")  #Imprimimos que se esta cargando el archivo
        except: #Si el archivo no existe
            print("Archivo no encontrado. Se creará uno nuevo.") # Muestra mensaje de error

    def aña_item(self, item):
        for i in self.items:  # Iteramos sobre la lista de items
            if i.get_id() == item.get_id():  # Verificamos si el ID ya existe
                print("Error: El ID ya existe.")  # Mensaje de error
                return
        self.items.append(item)  # Agregamos el nuevo item
        print("Producto añadido.")  # Mensaje de éxito

    def el_item(self, id_item):
        for i in self.items:  # Iteramos sobre la lista de items
            if i.get_id() == id_item:
                self.items.remove(i)  # Eliminamos el item
                print("Producto eliminado ")  # Mensaje de éxito
                return
        print("Error: no se encontro.")  # Mensaje de error

    def act_item(self, id_item, cantidad=None, precio=None):
        for i in self.items:  # Iteramos sobre la lista
            if i.get_id() == id_item:
                if cantidad is not None:  # Si la cantidad no es None
                    i.set_cantidad(cantidad)  # Actualizamos la cantidad
                if precio is not None:  # Si el precio no es None
                    i.set_precio(precio)  # Actualizamos el precio
                print("Item actualizado exitosamente.")  # Mensaje de éxito
                return
        print("Error: no encontrado.")  # Mensaje de error

    def bus_item(self, nombre):
        result = []  # Lista para los resultados
        for i in self.items:  # Iteramos sobre los items
            if nombre.lower() in i.get_nombre().lower():  # Verificamos si el nombre está contenido
                result.append(i)  # Añadimos el item a los resultados
        return result # Retornamos la lista de resultados

    def most_items(self):

            for i in self.items:  # Iteramos sobre los items
                print(
                    f"ID: {i.get_id()}, Nombre: {i.get_nombre()}, Cantidad: {i.get_cantidad()}, Precio: {i.get_precio()}")  # Mostramos los items


def mostrar():
    inventario = Inventario()
    while True:  # Bucle para el menú
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        try: # Comienza el bloque de manejo de errores
            opcion = input("Seleccione una opción: ") #Pedimos al usuario que ingrese una opcion

            if opcion == '1':  # Añadir producto
                id_item = input("Ingrese ID del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                item = Item(id_item, nombre, cantidad, precio)  #
                inventario.aña_item(item)

            elif opcion == '2':  # Eliminar producto
                id_item = input("Ingrese ID del producto a eliminar: ")
                inventario.el_item(id_item)

            elif opcion == '3':  # Actualizar producto
                id_item = input("Ingrese ID del item a actualizar: ")
                cantidad = input("Ingrese nueva cantidad : ")
                precio = input("Ingrese nuevo precio : ")
                inventario.act_item(id_item, int(cantidad) if cantidad else None,
                                            float(precio) if precio else None)

            elif opcion == '4':  # Buscar  producto
                id_item = input("Ingrese ID del producto a actualizar: ")
                cantidad = input("Ingrese nueva cantidad : ")
                precio = input("Ingrese nuevo precio : ")
                inventario.act_item(id_item, int(cantidad) if cantidad else None,
                                            float(precio) if precio else None)
                nombre = input("Ingrese nombre del item a buscar: ")
                resultados = inventario.bus_item(nombre)
                if resultados:  # Si hay resultados
                    for i in resultados:  # Iteramos sobre los resultados
                        print(
                            f"ID: {i.get_id()}, Nombre: {i.get_nombre()}, Cantidad: {i.get_cantidad()}, Precio: {i.get_precio()}")  # Mostramos los resultados
                else:
                    print("No se encontraron productos.")  # Mensaje de no encontrado

            elif opcion == '5':  # Mostrar items
                inventario.most_items()

            elif opcion == '6':  # Salir
                print("Saliendo.")
                break  # Salimos del bucle

        except ValueError:   # Verificamos si hay error al convertir números
            print("Error: Por favor ingrese números válidos para cantidad y precio.")  #Imprimimos un mensaje de qu eingrese
        except Exception as e: #Colcoamos otro except para ver si hay cualquier otro tipo de error
            print(f"Error: {str(e)}")  #Imprimimos que hay un error



prod = mostrar()
print(prod)