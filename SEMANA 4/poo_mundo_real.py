class Producto:  #Creamos la clase prodcuto
    def __init__(self, nombre, precio, cantidad_disponible):  #Creamos nuestro constructor y delaramos los atriubutos
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def agregar_al_carrito(self, cantidad):  #Creamos un metodo el cual nos permite agregar al carrito
        if self.cantidad_disponible >= cantidad:  #Creamos una condicion para verificar que la cantidad disponible sea mayor a la cantidad
            self.cantidad_disponible -= cantidad
            print(f"Se han agregado {cantidad} {self.nombre}(s) al carrito.")  #Imprimimos
        else:
            print(f"No hay suficientes {self.nombre}(s) disponibles.") #Sino se cumple imprimimos que no hay suficiente cantidad

    def calcular_total(self, cantidad):  #Creamos un metodo para calcular el total
        total = self.precio * cantidad
        return total

    def mostrar_resumen_compra(self, cantidad, total):  #Creamos un metodo para mostrar en pantalla las compras
        print(f"Resumen de la compra:")
        print(f"Producto: {self.nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Total: {total}")


#Instanciamos el objeto con la clase Producto
producto1 = Producto("Camisa", 20, 50)  #Llenamos los parametros de nuestra clase
producto1.agregar_al_carrito(3)  # Se han agregado 3 Camisa(s) al carrito.

cantidad_comprada = 5
total_compra = producto1.calcular_total(cantidad_comprada)
producto1.mostrar_resumen_compra(cantidad_comprada, total_compra)