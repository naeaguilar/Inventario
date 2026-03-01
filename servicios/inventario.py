from modelos.producto import Producto


class Inventario:
    def __init__(self):
        # Diccionario principal (clave = ID, valor = Producto)
        self.productos = {}
        self.cargar_desde_archivo()

    # ===============================
    # AGREGAR PRODUCTO
    # ===============================
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("⚠️ El ID ya existe.")
            return

        self.productos[producto.get_id()] = producto
        self.guardar_en_archivo()
        print("✅ Producto agregado.")

    # ===============================
    # ELIMINAR PRODUCTO
    # ===============================
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("🗑️ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    # ===============================
    # ACTUALIZAR PRODUCTO
    # ===============================
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]

            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)

            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)

            self.guardar_en_archivo()
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    # ===============================
    # BUSCAR POR NOMBRE (USA LISTA)
    # ===============================
    def buscar_producto(self, nombre):
        resultados = [
            producto for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]
        return resultados

    # ===============================
    # MOSTRAR TODOS
    # ===============================
    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for producto in self.productos.values():
            print(producto)

    # ===============================
    # OBTENER IDS (USA SET)
    # ===============================
    def obtener_ids(self):
        return set(self.productos.keys())

    # ===============================
    # GUARDAR EN ARCHIVO
    # ===============================
    def guardar_en_archivo(self):
        try:
            with open("inventario.txt", "w", encoding="utf-8") as archivo:
                for producto in self.productos.values():
                    archivo.write(producto.a_linea() + "\n")
            print("💾 Cambios guardados en archivo.")
        except PermissionError:
            print("❌ Error: No se tienen permisos para escribir el archivo.")

    # ===============================
    # CARGAR DESDE ARCHIVO
    # ===============================
    def cargar_desde_archivo(self):
        try:
            with open("inventario.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    producto = Producto.desde_linea(linea)
                    self.productos[producto.get_id()] = producto
        except FileNotFoundError:
            # Si no existe, lo crea vacío
            with open("inventario.txt", "w", encoding="utf-8"):
                pass
        except Exception as e:
            print("❌ Error al cargar archivo:", e)