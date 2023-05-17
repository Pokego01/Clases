## Numeros Enteros del 1 a infinito, no incluye decimales
## Numeros Reales todo numero, incluidos los decimales
## Numeros imaginarios raices de numeros negativos
##int redondeara los numeros decimales a enteros
##round tambien los redondeara a un entero
##float mostrara todos los numeros enteros como decimales
Peso=70.5
Edad=29
Estatura=1.71
print("tu peso es", int(Peso))
print("tu Estatura es", Estatura)
nombre = input("CUAL ES TU NOMBRE?\n")
edad = int(input("CUAL ES TU EDAD?\n"))
print("Mi nombre es", nombre, "mi edad es", edad, "años y en 20 años tendre", edad+20, "años")
float(Estatura)
print("tu edad es", float(Edad))

imc = Peso/(Estatura**2)
print("Mi IMC es de:", (imc))
## {:.2f}".format(imc) sirve para definir la cantidad de numeros en decimal y en que aplicarlo
print("Mi IMC es de: {:.2f}".format(imc),"\n")

asignatura = 'Programación'
Carrera = "Ingenieria Cicil en Informatica"
print("la asignatura de", asignatura, "es de la carrera:", Carrera)
## len sirve para contar cararcteres de una variable 
##Los esp{:.2f}".format(imc)acion cuentan como caracteres
print("Los caracteres de la palabra", Carrera, "Son:", len(Carrera))

##Falso simpre sera 0 en tipo bool y verdadero sera 1
ampolleta = False
interruptor = True
print(ampolleta, interruptor)
## type sirve para reconocer el tipo de variable
print("La variable ampolleta es de tipo", type(ampolleta))
print(bool(0))
print(bool(""))
print(bool(None))
print(bool(True))
print(bool(1))

## list sera usado para crear listas y guardar variables
## PARA CREAR UNA LISTA USAREMOS: list() o []
nueva_lista = list()
otra_lista = []
print("ESTA ES UNA NUEVA LISTA VACIA", nueva_lista)
print("ESTA ES UNA OTRA LISTA VACIA", otra_lista)
Estudiantes = ["Marco", "Juan", "Seba", "Matias", "Juan"]
num = [1,2,3,4,5,6,1]
lenguaje = ["Python"]
data = ["Marvel", "Pato", "657", "Paralelepipedo", "Supercalifragilisticoespiralidoso"]
nombre = input("CUAL ES TU NOMBRE?\n")
edad = int(input("CUAL ES TU EDAD?\n"))
print("Mi nombre es", nombre, "mi edad es", edad, "años y en 20 años tendre", edad+20, "años")
## count se usa para contar la cantidad de variables con el mismo nombre en una lista
print(Estudiantes.count("Juan"))
print(num.count(1))
## Se puede buscar un elemento que se encuentre o no, en caso de no haber este marcara 0
print(Estudiantes.count("Pedro"))

##De la siguiente manera podremos buscar el valor guardado en una lista en una posicio en especifica
print(Estudiantes[0])
## 0 sera el primer valor guardado, 1 el segundo y así en adelante
print(Estudiantes[1])
##Al usar un numero negativo este empezara contando desde el final al inicio
print(data[-1])

##Tuplas
newtuple = tuple()
##Las tuplas usan parentesis
grupo1 = ("daniel","constanza","4354654","4554")
print(grupo1[0])
##grupo1[0]= "constanza" no es valido ni apollado por tupla
##las tuplas son inmutables lo que hace que no puedadn ser modificadas a diferencia de las listas
grupo2=("pedro",121,"juan", "diego", 4654, "alejandro")
print("trozo de la tupla", grupo2[0:3])
## de esta forma se leera todo dato desde el 0 a 3

##Sets(conjuntos)
conjunto_vacio = set()
conjunto_vacio1={}
color = set({"azul", "rojo", "5.63}amarillo", "Magenta"})
animal = {"perro", "loro", "vaca", "tigre"}
print(type(color))
print("el set contiene los siguientes animales", animal)
#add se usa para añadir un elemento al conjunto
animal.add("mariposa")
print("el set contiene los siguientes animales ahora", animal)
## no se puede guardar la posicion de los elementos, pues estos estan almacernados de manera aleatoria

##Diccionario
diccionario1 = dict()
diccionario2 = {}
datos_personales = {
    "nombre":"victor",
    "Institucion":"Ulagos",
    "Asignaturas":{"Programación", "Estructura de datos"}}

print("diccionario inicial:", datos_personales)
datos_personales["Ciudad"] = "Osorno" #PARA AÑADIR DEF. A DICCIONARIO
