from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n" + "=" * 45)
    print("         SISTEMA DE RESTAURANTE")
    print("=" * 45)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 45)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 45)
    print("7. Salir")


def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))

                producto = Producto(
                    nombre,
                    categoria,
                    precio
                )

                restaurante.registrar_producto(producto)

                print("Producto registrado correctamente.")

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            restaurante.listar_productos()

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")

            producto = restaurante.buscar_producto(nombre)

            if producto:
                print(producto.mostrar_informacion())
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del cliente: ")
            correo = input("Correo: ")
            id_cliente = int(input("ID del cliente: "))

            cliente = Cliente(
                nombre,
                correo,
                id_cliente
            )

            restaurante.registrar_cliente(cliente)

            print("Cliente registrado correctamente.")

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            id_cliente = int(
                input("Ingrese el ID del cliente: ")
            )

            cliente = restaurante.buscar_cliente(id_cliente)

            if cliente:
                print(cliente)
            else:
                print("Cliente no encontrado.")

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()