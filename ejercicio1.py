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