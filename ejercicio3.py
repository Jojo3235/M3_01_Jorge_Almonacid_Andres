#Ejercicio 3

class Producto():       #Creamos la clase Producto
    def __init__(self,codigo,nombre,precio,tipo):    #Creamos el constructor en base a los atributos codigo, nombre, precio y tipo 
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        print("El producto ha sido creado con éxito")   #Cuando se ejecuta la función printamos que se ha creado el producto con éxito
    
    def __str__(self):      #Creamos una función que cuando mandemos printar nuestro elemento de la clase nos imprima lo definido en la línea siguiente
        return "Código: {}\nNombre: {}\nPrecio: {}\nTipo: {}".format(self.codigo,self.nombre,self.precio,self.tipo)

#Creamos distintos objetos dentro de la clase y los imprimimos 
prod1=Producto("01","Botón de camiseta","0.10€","Botón")  
print(prod1)
prod2=Producto("10","Portátil","799,90€","Ordenador")
print(prod2)
prod3=Producto("11","Chaqueta","15€","Ropa")
print(prod3)
prod3.nombre="Pantalón"     #Cambiamos el atributo nombre y precio y volvemos a printar
prod3.precio="10€"
print(prod3)