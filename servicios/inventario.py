# Maneja las operaciones del inventario

from modelos.producto import Producto


class Inventario:
    def __init__(self):
        # Lista principal de almacenamiento
        self.productos = []

    # Añadir producto
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("⚠️ El ID ya existe.")
                return
        self.productos.append(producto)
        print("✅ Producto agregado.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑 Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_producto(self, nombre):
        resultados = []
        nombre = nombre.lower()

        for p in self.productos:
            if nombre in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    # Mostrar todos
    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for p in self.productos:
            print(p)
