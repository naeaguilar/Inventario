# Menú principal del sistema

from servicios.inventario import Inventario
from modelos.producto import Producto


def menu():
    print("\n=== SISTEMA DE INVENTARIO ===")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            except ValueError:
                print("⚠️ Datos inválidos.")

        elif opcion == "2":
            id_producto = input("Ingrese ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto: ")

            try:
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(
                    id_producto,
                    nueva_cantidad,
                    nuevo_precio
                )

            except ValueError:
                print("⚠️ Datos inválidos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
