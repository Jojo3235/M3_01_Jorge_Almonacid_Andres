#Ejercicio 1

class Alumno():     #Creamos la clase alumno
    def __init__(self, nombre, nota):   #Le asignamos los atributos de nombre y nota y devolvemos si el alumno se creo de manera exitosa
        self.nombre=nombre
        self.nota=nota
        print("El alumno se ha creado con éxito")
    
    def calificación(self):  #Creamos una función con la cual vemos si el atributo nota es mayor o igual a 5 y nos devuelve si está aprobado o no
        if (self.nota)>=5:
            print("El alumno está aprobado")
        else:
            print("El alumno está suspenso")


alumno1=Alumno("Pedro",8) #Creamos distintos objetos con distintos atributos y comprobamos si están aprobados o suspensos
alumno1.calificación()
alumno2=Alumno("José",6)
alumno2.calificación()
alumno3=Alumno("Víctor",7)
alumno3.calificación()
alumno4=Alumno("Fernando",4)
alumno4.calificación()

#Ejercicio 2

class Alumno():     #Creamos la clase alumno
    def __init__(self, nombre, nota):   #Le asignamos los atributos de nombre y nota y devolvemos si el alumno se creo de manera exitosa
        self.nombre=nombre
        self.nota=nota
        print("El alumno se ha creado con éxito")
    
    def calificación(self):  #Creamos una función con la cual vemos si el atributo nota es mayor o igual a 5 y nos devuelve si esta aprobado o no
        if (self.nota)>=5:
            print("El alumno está aprobado")
        else:
            print("El alumno está suspenso")
    
    def __str__(self):
        return "Alumno:{}\nNota:{}".format(self.nombre,self.nota)

alumno1=Alumno("Pedro",8) #Creamos distintos objetos con distintos atributos y printamos sus atributos
print(alumno1)
alumno2=Alumno("José",6)
print(alumno2)
alumno3=Alumno("Víctor",7)
print(alumno3)
alumno4=Alumno("Fernando",4)
print(alumno4)

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