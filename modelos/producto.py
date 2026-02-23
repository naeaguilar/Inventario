# Representa un producto dentro del inventario

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Representación para mostrar en pantalla
    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"

    # Convertir producto a formato archivo
    def a_linea_archivo(self):
        return f"{self.__id}|{self.__nombre}|{self.__cantidad}|{self.__precio}"

    # Reconstruir producto desde archivo
    @staticmethod
    def desde_linea(linea):
        try:
            partes = linea.strip().split("|")
            return Producto(
                partes[0],
                partes[1],
                int(partes[2]),
                float(partes[3])
            )
        except (ValueError, IndexError):
            print("⚠ Línea inválida en archivo:", linea.strip())
            return None