from math import prod


class Producto():
    def __init__(self,codigo,nombre,precio,tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        print("El producto ha sido creado con éxito")
    
    def __str__(self):
        return "Código: {}\nNombre: {}\nPrecio: {}\nTipo: {}".format(self.codigo,self.nombre,self.precio,self.tipo)

prod1=Producto("01","Botón de camiseta","0.10€","Botón")
print(prod1)
prod2=Producto("10","Portátil","799,90€","Ordenador")
print(prod2)
prod3=Producto("11","Chaqueta","15€","Ropa")
print(prod3)
prod3.nombre="Pantalón"
prod3.precio="10€"
print(prod3)