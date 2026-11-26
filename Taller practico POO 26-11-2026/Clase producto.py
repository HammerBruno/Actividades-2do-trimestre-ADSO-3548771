class Producto:

    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo= codigo
        self.nombre= nombre
        self.precio= precio
        self.cantidad= cantidad

    def mostrar_informacion(self):

        print("codigo:", self.codigo)
        print("nombre:", self.nombre)
        print("precio:", self.precio)
        print("cantidad:", self.cantidad)

    def actualizar_precio(self, nuevo_precio):

        self.precio = nuevo_precio

    def aumentar_existencias(self, cantidad):
        if cantidad > 0:

            self.cantidad += cantidad

producto1 = Producto(101, "teclado", 80000, 10)

producto2 = Producto(102, "mouse", 45000, 15)

producto1.mostrar_informacion()

producto2.mostrar_informacion()

producto1.actualizar_precio(85000)

producto2.aumentar_existencias(5)

producto3 = Producto(103, "bocina", 30000, 5)

producto1.mostrar_informacion()

producto2.mostrar_informacion()

producto3.mostrar_informacion()

producto3.actualizar_precio(35000)

producto1.aumentar_existencias(3)

producto1.mostrar_informacion()

producto2.mostrar_informacion()

producto3.mostrar_informacion()

        

