# Maneja las operaciones del inventario

from modelos.producto import Producto


class Inventario:
    def __init__(self):
        self.archivo = "inventario.txt"
        self.productos = []
        self.cargar_desde_archivo()

    # Cargar productos desde archivo
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    producto = Producto.desde_linea(linea)
                    if producto:
                        self.productos.append(producto)
            print("📂 Inventario cargado correctamente.")
        except FileNotFoundError:
            print("📁 Archivo no existe. Se creará uno nuevo.")
            open(self.archivo, "w").close()
        except PermissionError:
            print("❌ No tienes permisos para leer el archivo.")

    # Guardar productos en archivo
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for producto in self.productos:
                    f.write(producto.a_linea_archivo() + "\n")
            print("💾 Cambios guardados en archivo.")
        except PermissionError:
            print("❌ No tienes permisos para escribir en el archivo.")

    # Añadir producto
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("⚠️ El ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto agregado.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
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

                self.guardar_en_archivo()
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