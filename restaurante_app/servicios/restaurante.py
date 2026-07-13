class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    # PRODUCTOS

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        if not self.productos:
            print("No existen productos registrados.")
            return

        for producto in self.productos:
            print("-" * 40)
            print(producto.mostrar_informacion())

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    # CLIENTES

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        if not self.clientes:
            print("No existen clientes registrados.")
            return

        for cliente in self.clientes:
            print("-" * 40)
            print(
                f"ID: {cliente.id_cliente}\n"
                f"Nombre: {cliente.nombre}\n"
                f"Correo: {cliente.correo}"
            )

    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None